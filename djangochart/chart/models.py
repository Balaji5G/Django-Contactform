from django.db import models
from django.db.models.fields import UUIDField
import uuid

# Create your models here.
class base(models.Model):
    Id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    City=models.CharField(max_length=50)
    Temperature=models.FloatField(max_length=150)
    Timestamp=models.CharField(max_length=50) 

    
    def __str__(self):
        return self.City


    