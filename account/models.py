from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class UserApi(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    api_key = models.CharField(max_length=80,blank=True,null=True)
    
    def save(self,*args,**kwargs):
        self.api_key =  str(uuid4())
        super(UserApi, self).save(*args, **kwargs)    
    def __str__(self)->str:
        return self.user.username

