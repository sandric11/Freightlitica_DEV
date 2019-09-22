from django.urls import path
from . import views

myapp_calc = 'calculator'

urlpatterns = {
   # path('', views.post_list, name='postlist'),
    path('', views.index, name='index'),
}
