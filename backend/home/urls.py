
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),  #  http://127.0.0.1:8000/api/
    path('api/products/',include('products.urls')), 
]
