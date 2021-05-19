"""CTFtool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.button),
    path('', views.home, name = "home"),
    path('output/', views.abc, name = "abc"),
    path('us/', views.us, name = "us"),
    path('base64d/', views.b64d),
    path('base64e/', views.b64e),
    path('base86d/', views.b86d),
    path('base86e/', views.b86e),
    path('base32d/', views.b32d),
    path('base32e/', views.b32e),
    path('caesard/', views.caeserd),
    path('caesare/', views.caesere),
    path('morsed/', views.morsed),
    path('morsee/', views.morsee),
    path('bacond/', views.bacond),
    path('bacone/', views.bacone),
    path('vigenered/', views.vigenered),
    path('vigeneree/', views.vigeneree),
    path('sherlock/', views.sherlock),
    path('rotd/', views.rotd),
    path('rote/', views.rote),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
