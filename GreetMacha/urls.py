"""GreetMacha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from templates import views as template_views
from userDetails import views as userDetails_views
from templates import views as templates_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage url requests
    path('', template_views.home, name='home'),
    path('tp_1', userDetails_views.formpage, name='details'),
    path('bday', userDetails_views.bdaypage, name='birthday'),
    path('template_01', templates_views.t1, name='birthday_template')

]

urlpatterns += staticfiles_urlpatterns()
