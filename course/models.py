from django.db import models
from tutor.models import Tutor
tutor=models.ForeignKey(Tutor,null=True,on_delete=models.CASCADE)
# Create your models here.
class Course(models.Model):
	name=models.CharField(max_length=100)
	duration_in_months=models.SmallIntegerField()
	start_date=models.DateField()
	end_date=models.DateField()
	description=models.TextField()


	def __str__(self):
		return self.name


