from django.urls import path, include

from .views import *
from .viewsets import ArticleViewSet
from .routers import router


"""
- 'api/v1/', include('rest_framework.urls') - реализация авторизации на основе сессий;
- последующие адреса, начинающиеся с api/v1/, демонстрируют работу CRUD-представлений,
   наследованных от generics.APIView;
- адреса, начинающиеся с api/v2/, демонстрируют работу ViewSet, реализующего в себе
   функционал вышеуказанных представлений. Ключ содержит тип запроса, значение ключа
   указывает, какой метод класса ViewSet надо вызвать для этого запроса;
- 'api/v3/' реализует вызов вышеуказанного ViewSet через роутер.

"""


urlpatterns = [
	path('', main_page, name='main_page_url'),
	path('<slug:slug>/', ArticleDetail.as_view(), name='item_page_url'),
	path('api/v1/', include('rest_framework.urls')),
	path('api/v1/artlist/', ArticleAPIList.as_view()),
	path('api/v1/artlist/<int:pk>/', ArticleAPIUpdate.as_view()),
	path('api/v1/artdetail/<int:pk>/', ArticleAPIDetail.as_view()),
	path('api/v1/artdelete/<int:pk>/', ArticleAPIDestroy.as_view()),
	path('api/v2/artlist/', ArticleViewSet.as_view({'get': 'list'})),
	path('api/v2/artcreate/', ArticleViewSet.as_view({'post': 'create'})),
	path('api/v2/artupdate/<int:pk>/', ArticleViewSet.as_view({'put': 'update'})),
	path('api/v2/artdelete/<int:pk>/', ArticleViewSet.as_view({'delete': 'destroy'})),
	path('api/v3/', include(router.urls)),
]