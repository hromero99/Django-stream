from django.db import models
from django.contrib.auth.models import User
from events.models import Event
import uuid

class EventTicket(models.Model):

    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4().hex)
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    owner_id = models.OneToOneField(User,on_delete=models.RESTRICT)