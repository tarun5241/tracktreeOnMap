from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Ngo
# Create your models here.

# @receiver(post_save, sender=Profile) # another way of producing signals like "post_save.connect()"
def profileCreated(sender, instance, created, **kwargs):    
    print("Profile Signal triggered")
    if created:
        user = instance
        name=user.username
        email=user.email
        # form = Ngo(name=name,email=email)
        # form.save()
        profile = Ngo.objects.create(name = user, email=user.email)
        print("Profile Created")
    print("Instance", instance)
    print("Created", created)


# def profileDeleted(sender, instance, **kwargs):
#     user = instance.user
#     user.delete()
#     # print("Deleting User ....")


post_save.connect(profileCreated, sender=User)


# post_delete.connect(profileDeleted,sender=Ngo)