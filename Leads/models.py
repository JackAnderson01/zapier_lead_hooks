from django.db import models
import uuid

# Create your models here.
class Leads(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    barkId = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.barkId