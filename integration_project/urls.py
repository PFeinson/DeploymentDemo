"""integration_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import apps
import apps.integrationProject.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ninjaGold/', include('apps.ninjaGold.urls')),
    url(r'^time/', include('apps.timedisplay.urls')),
    url(r'^ranWord/', include('apps.randWordGen.urls')),
    url(r'^courses/', include('apps.coursesApp.urls')),
    url(r'^$', apps.integrationProject.views.index),
    url(r'^loginAndReg/', include('apps.loginAndReg.urls')),

]
