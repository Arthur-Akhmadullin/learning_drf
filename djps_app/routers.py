from rest_framework import routers

from .viewsets import ArticleViewSet

"""
Для того, чтобы в файле urls.py не расписывать все маршруты Viewset'а, можно определить
маршрутизатор (роутер).
Роутер самостоятельно определяет вызов нужного метода в зависимости от типа маршрута.
Адрес строится по типу: http://127.0.0.1:8000/api/v1/<название модели в нижнем регистре>/.

***Документация:***
https://www.django-rest-framework.org/api-guide/routers/

"""


router = routers.SimpleRouter()
router.register(r'article', ArticleViewSet)