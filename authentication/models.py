from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model) : 
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	regNum = models.CharField(max_length=10)
	contact = models.DateTimeField(max_length=20)

	def __str__(self):
		return (self.user.first_name + "_" + self.regNum)
