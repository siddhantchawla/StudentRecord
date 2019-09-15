from django.db import models
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime   


# Create your models here.
class Record(models.Model):
	regNum = models.CharField(max_length=10) 
	status = models.IntegerField()
	date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return ("Reg No. - "+self.regNum+" Date: "+str(self.date))
