from django.db import models


# Create your models here.
class storedInformation(models.Model):
	rid=models.CharField(max_length=10)
	forminfo= models.TextField()
	
class Meta:
	db_table='template_display'
