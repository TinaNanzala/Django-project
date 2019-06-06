from django.db import models

# Create your models here.
class Tutor(models.Model):
	first_name=models.CharField(max_length=60)
	last_name=models.CharField(max_length=60)
	tutor_hour=models.DateField()
	gender=models.CharField(max_length=20)
	staff_number=models.CharField(max_length=20)
	email=models.EmailField(max_length=70)
	contact=models.CharField(max_length=20)
	date_employed=models.DateField(null=True)
	id_number=models.SmallIntegerField(null=True)
	Professsion=models.CharField(max_length=60,null=True)
	phone_number=models.CharField(max_length=20,null=True)

	def __str__(self):
		return self.first_name




