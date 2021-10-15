from django.db import models
from django.conf import settings
# Create your models here.

class Image(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)

	title=models.CharField(max_length=40)
	slug=models.SlugField(max_length=40,unique=True, blank=True)

	url=models.URLField()
	description=models.TextField()
	image=models.ImageField(upload_to='images/%Y/%m/%d/')
	created=models.DateField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.title