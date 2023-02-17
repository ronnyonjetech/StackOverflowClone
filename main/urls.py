from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.main,name='main'),
    path('detail/<int:id>', views.detail,name='detail'),

]