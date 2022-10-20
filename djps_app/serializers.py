from rest_framework import serializers

from .models import Article


"""
***Документация:***
https://www.django-rest-framework.org/api-guide/serializers/

"""


class ArticleSerializer(serializers.ModelSerializer):
	#автоматическое заполнение поля "user" модели "Article" при создании записи
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Article
		fields = "__all__"