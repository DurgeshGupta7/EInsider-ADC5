from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class File(models.Model):
	title = models.CharField(max_length = 100)
	file_type= models.CharField(max_length=100)
	file = models.FileField(upload_to='files/')

	def __str__(self):
		return self.title


	def delete(self,*args,**kwargs):
		self.file.delete()
		super().delete(*args,**kwargs)






