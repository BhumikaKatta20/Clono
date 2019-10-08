from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	Address=models.TextField(default='')
	city=models.CharField(max_length=100,default='')
	phone=models.IntegerField(default=0)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

class marks(models.Model):
	round1=models.IntegerField(default=0)
	round2=models.IntegerField(default=0)
	round3=models.IntegerField(default=0)
	round4=models.IntegerField(default=0)
	total=models.IntegerField(default=0)
	precentage=models.IntegerField(default=0)

