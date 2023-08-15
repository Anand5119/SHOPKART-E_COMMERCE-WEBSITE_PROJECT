
from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('collection', views.Collections, name='collection'),
    path('collectionItem/<str:name>', views.colectionItem, name='collections'),
    path('productDetails/<str:cname>/<str:pname>',
         views.productDetails, name='productDetails')
]
