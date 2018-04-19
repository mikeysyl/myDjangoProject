from django.db import models
from  django.conf import settings

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	title =models.CharField(max_length=120)
	slug = models.SlugField(max_length=120, unique=True)
#	image = models.ImageField(upload_to='records')
	content=models.TextField()
	draft = models.BooleanField(default=False)
	updated= models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title