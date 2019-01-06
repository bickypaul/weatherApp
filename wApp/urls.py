from django.urls import path
from . import views


# all the urls are self descriptive.
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<city_id>', views.deleteCity, name='delete-city'),
    path('deleteall/', views.deleteAll, name='delete-all')
]
