from rest_framework import viewsets

from .models import Article
from .serializers import ArticleSerializer
from .views import ArticleAPIListPagination


"""
В файле views.py имеем дублирующийся код в предсталениях:
ArticleAPIList
ArticleAPIDetail
ArticleAPIUpdate
ArticleAPIDestroy

Для устранения подобного кода его выносят в ViewSet.

***Документация:***
https://www.django-rest-framework.org/api-guide/viewsets/

"""


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleAPIListPagination