from django.db import models
import uuid

class Event(models.Model):

    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4().hex)
    name = models.CharField(max_length=20)
    description = models.TextField()

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description
        }