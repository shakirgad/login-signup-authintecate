from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User  ,on_delete=models.CASCADE)
    phone_number=models.CharField( max_length=15 ,blank=True, null=True)
    addres=models.CharField( max_length=50 ,blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
    
@receiver(post_save , sender=User) 
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(
            user=instance
        )
    #instance.profile.save()