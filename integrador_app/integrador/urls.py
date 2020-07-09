from django.urls import path
from . import views

app_name = 'integrador'
urlpatterns = {
    path('', views.index, name = 'index'),
    path('integrador', views.index, name = 'index')
}