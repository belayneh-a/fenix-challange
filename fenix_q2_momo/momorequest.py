import oauth2,uuid,json,sys
import requests
from .models import MomoRequests,MomoCredentials

class MomoRequest:
    xreference_id = uuid.uuid1()
    header = {'Authorization': '','X-Callback-Url': '','X-Reference-Id': xreference_id, 'X-Target-Environment': '',
        'Content-Type': 'application/json','Ocp-Apim-Subscription-Key': '', }
    body = {'amount': '', 'currency':'', 'externalId': '','payer': {'partyIdType': '','partyId': ''},
            'payerMessage': '','payeeNote': ''}


    def __init__(self,amount,currency,externaid,partyid,payermsg,payenote,partyidtype='MSISDN'):
        credentials = MomoCredentials.load()
        self.header['Ocp-Apim-Subscription-Key'] = credentials.subscription_key
        self.body['amount'] = sys.argv[1]
        self.body['currency'] = sys.argv[2]
        self.body['externalId'] = sys.argv[3]
        self.body['payerMessage'] = sys.argv[4]
        self.body['payeeNote'] = sys.argv[5]
        self.body['partyidtype'] = sys.argv[6]
        self.body['partyId'] = sys.argv[7]

        try:
            consumer = oauth2.Consumer(key = credentials.id, secret = credentials.key)
            client = oauth2.Client(consumer)
            momo_token_req = 'https://ericssonbasicapi2.azure-api.net/collection/token/'
            resp, content = client.request(momo_token_req)
            resp_res = json.loads(content)

            if resp_res['statusCode'] == 200:
                token = resp_res['access_token']
                requesttopay_uri = 'https://ericssonbasicapi2.azure-api.net/collection/v1_0/requesttopay'
                resp_res = requests.post(requesttopay_uri, params=self.body, headers=self.header)
                resp_json = json.loads(resp_res)
                if resp_json['statusCode'] == 200:
                   self.register_to_db()


        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


    def register_to_db(self):
        new_request = MomoRequests(amount=self.body['amount'], currency=self.body['currency'],
                                   external_id=self.body['externaid'],
                                   partyIdType=self.body['partyidtype'], partyId=self.body['partyId'],
                                   payerMessage=self.body['payerMessage'], payeeNote=self.body['payeeNote'],
                                   referance_id=self.body['reference_id'], status='PENDING')
        new_request.save()


if __name__ == '__main__':

    new_requests = MomoRequest()


