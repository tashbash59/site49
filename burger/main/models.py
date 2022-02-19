from django.db import models
from django.conf import settings
from django.utils import timezone

class New(models.Model):
	NewsPost = models.CharField(max_length =200)
	text = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.NewsPost

	class Meta:
		ordering = ['-published_date']


class Galery(models.Model):
	title = models.CharField(max_length = 150, null = True)
	Photo = models.ImageField(upload_to = 'images/')

	def __str__(self):
		return self.title
