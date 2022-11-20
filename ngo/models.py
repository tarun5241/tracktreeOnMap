import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ngo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    email = models.EmailField(max_length = 254)
    ngo_name = models.TextField(null=True, blank=True)
    mission = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    total_member = models.IntegerField(default=0,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

#to encrypt the models in database to view the tables in db
    def __str__(self):
        return self.email
    

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    ngo_name = models.ForeignKey(Ngo,on_delete=models.CASCADE,null=True,blank=True)
    # email = models.EmailField(max_length = 254)
    event_name = models.CharField(max_length=30, null=True, blank=True)
    event_date = models.DateField(null=True,blank=True)
    tree_name = models.CharField(max_length=30, null=True, blank=True)
    trees_planted = models.CharField(max_length=30, null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)


#to encrypt the models in database to view the tables in db
    def __str__(self):
        return self.event_name
    
    
