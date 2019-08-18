from django.db import models

class MomoRequests(models.Model):
    amount = models.CharField(max_length=100),
    currency = models.IntegerField(),
    external_id = models.CharField(max_length=100),
    target_env = models.CharField(max_length=100),
    partyIdType = models.CharField(max_length=10),
    partyId = models.CharField(max_length=20),
    payerMessage = models.CharField(max_length=200),
    payeeNote = models.CharField(max_length=200),
    reference_id = models.CharField(max_length=100),
    status = models.CharField(max_length=10)

class MomoCredentials(models.Model):
    id = ['id_field'],
    key = ['key_field'],
    subscription_key = ['subscription_key_field'],
