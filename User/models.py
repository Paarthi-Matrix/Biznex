import datetime
import uuid
from django.db import models


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    name = models.CharField(max_length=30, null=False)
    mobile_number = models.CharField(max_length=10, null=False)
    email_id = models.CharField(max_length=320, null=False)
    gender = models.CharField(max_length=11, null=False)
    date_of_birth = models.DateField(max_length=10, null=False, default=datetime.date(1000, 1, 1))
    password = models.CharField(max_length=256, null=False)

