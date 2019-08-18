import requests,json
from .models import MomoRequests,MomoCredentials
from .celery import app as Celery_app

apdate_tsk= Celery_app('app', broker='amqp://locahost//')

header = {'Authorization': '', 'X-Target-Environment': '',
          'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': ''}
body = {'X-Reference-Id': ''}


def get_pending_requests():
    credentials = MomoCredentials.load()
    header['Ocp-Apim-Subscription-Key'] = credentials.subscription_key

    pending_req = MomoRequests.objects.filter(status='PENDING')
    return pending_req


@apdate_tsk.task
def check_status_n_update():
    pending_requests = get_pending_requests()
    for status, pending_payment in pending_requests.items():
        body['X-Reference-Id'] = status[pending_payment]['reference_id']
        get_status_uri = 'https://ericssonbasicapi2.azure-api.net/collection/v1_0/requesttopay/{referenceId}'
        resp_res = requests.get(get_status_uri, params=body, headers=header)
        resp_json = json.loads(resp_res)
        if resp_json['statusCode'] == 200 and resp_json['status'] == 'SUCCESS':
            update_req = MomoRequests.objects.filter(reference_id=body['X-Reference-Id'])
            update_req.status = 'SUCCESS'
            update_req.save()
