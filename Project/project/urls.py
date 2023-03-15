from django.contrib import admin
from django.urls import path
from mysite import views

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('shopping_detail/',views.shopping_detail,name='shopping_detail'),
    path('form/',views.form_name_view,name='form')
]


