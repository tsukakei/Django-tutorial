from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^v1/books/$', views.book_list, name='book_list'),
]
