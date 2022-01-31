from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    name=models.CharField(max_length=256)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.OneToOneField(User,on_delete=models.CASCADE)


    class Meta:
        ordering=['name']
    
    def __str__(self):
        return str(self.name)