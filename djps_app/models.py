from django.db import models
from django.contrib.auth.models import User

from django.shortcuts import reverse


class Article(models.Model):
	title = models.CharField(max_length=250, db_index=True)
	slug = models.SlugField(max_length=250, unique=True)
	body = models.TextField(blank=True)
	date = models.DateField(auto_now_add=True)
	category = models.ForeignKey('Category', related_name='cat', on_delete=models.PROTECT, null=True)
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('item_page_url', kwargs={'slug': self.slug})
		
	class Meta:
		ordering = ['-date']


class Category(models.Model):
	category = models.CharField(max_length=30)
	slug = models.SlugField(max_length=30, unique=True)

	def __str__(self):
		return self.category