"""geekshop DD Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from geekshop.views import index, contacts

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    # path('admin/', include('authapp.urls', namespace='auth'), name='auth'),
    path('products/', include('mainapp.urls', namespace='products'), name='products'),
    path('admin_staff/', include('adminapp.urls', namespace='admin_staff'), name='admin_staff'),
    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
    path('basket/', include('basketapp.urls', namespace='basket'), name='basket'),
    path('contacts/', contacts, name='contacts'),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
