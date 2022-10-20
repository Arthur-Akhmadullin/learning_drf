from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, \
	RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.pagination import PageNumberPagination


from .models import Article
from .serializers import ArticleSerializer


"""
***Документация:***
https://www.django-rest-framework.org/api-guide/generic-views/

"""


def main_page(request):
	articles = Article.objects.all()
	context = {'articles': articles}	
	return render(request, 'djps_app/index.html', context)
	
	
class ArticleDetail(View):
	def get(self, request, slug):
		item = get_object_or_404(Article, slug__iexact=slug)
		return render(request, 'djps_app/detail.html', {'item': item})


#Количество выводимых записей
class ArticleAPIListPagination(PageNumberPagination):
	page_size = 2
	page_size_query_param = 'page_size'
	max_page_size = 10000


class ArticleAPIList(ListCreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	permission_classes = (IsAuthenticatedOrReadOnly, )
	pagination_class = ArticleAPIListPagination

	
class ArticleAPIUpdate(UpdateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	permission_classes = (IsAuthenticatedOrReadOnly, )
	pagination_class = ArticleAPIListPagination


class ArticleAPIDetail(RetrieveUpdateDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	permission_classes = (IsAuthenticatedOrReadOnly, )


class ArticleAPIDestroy(RetrieveDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	permission_classes = (IsAdminUser, )



