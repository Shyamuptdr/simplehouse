from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('register/', views.register),
    path('verify/', views.verify),   
    path('login/', views.login),
    path('contact/', views.contact),
    path('myadmin/', views.adminhome),
    path('cpadmin/', views.cpadmin),
    path('manageusers/', views.manageusers),
    path('manageuserstatus/', views.manageuserstatus),
    path('user/', views.userhome),
    path('cpuser/', views.cpuser),
    path('sharerecipe/', views.sharerecipe),
    path('viewrecipe/', views.viewrecipe),
    path('order/', views.order),
    path('payment/', views.payment),
    path('success/', views.success),
    path('cancel/', views.cancel)
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
