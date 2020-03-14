from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
	title = models.CharField(max_length = 120)
	post = models.TextField()
	date = models.DateTimeField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title