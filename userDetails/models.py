from django.db import models

# Create your models here.
class formInformation(models.Model):
	name=models.CharField(max_length=30)
	date=models.CharField(max_length=10)
class Meta:
	db_table='userDetails'




