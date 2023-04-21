from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class ImageModel(models.Model):
    uuid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="images",null=True,blank=True)
    image = models.ImageField(upload_to='images/')
    watermark_text = models.CharField(max_length=150)
    watermraked_image = models.ImageField(upload_to='output/',null=True)
