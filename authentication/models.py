from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model) : 
	branch_choices = (
		('CSE','Computer Science & Engineering'),
		('ECE','Electronics and Communication Engineering'),
		('MECH','Mechanical Engineering'),
		('MME','Metallurgy Engineering'),
		('CHE','Chemical Engineering'),
		('CIVIL','Civil Engineering'),
		('EEE','Electrical and Electronics Engineering'),
		('BIO','Biotechnology'),
	)

	course_choices = (
		('BTech','B.Tech'),
		('MTech','M.Tech'),
		('MCA','MCA'),
		('MBA','MBA'),
		('PHD','Phd'),
	)

	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	regNum = models.CharField(max_length=10)
	course = models.CharField(max_length=10,choices = course_choices,default='BTech')
	branch = models.CharField(max_length=10,choices = branch_choices)
	contact = models.CharField(max_length=20)

	def __str__(self):
		return (self.user.first_name + "_" + self.regNum)
