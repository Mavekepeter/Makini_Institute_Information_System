from django.urls import path
from . import views as stephen

urlpatterns = [
    path('add_course/', stephen.add_course, name='add_course-url'),
    path('view_course/', stephen.products, name='views_course-url'),
    path('buy_course/<id>', stephen.Buy_course, name='Buy_course-url'),
    path('delete_course/<id>', stephen.delete, name='delete-url'),
]
