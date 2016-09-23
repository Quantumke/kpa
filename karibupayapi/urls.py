"""karibupayapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import *
from django.contrib import admin
from mpesa import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sub/', views.register_sandbox_user, name='register_sandbox_user'),
    url(r'^confirmaccount/', views.confirm_account, name='confirm_account'),
    url(r'^$', views.home, name='home'),
    url(r'^sendpayment/', views.invoke_payment, name='invoke_payment'),
    url(r'^invoke/', views.get_responses, name='get_responses'),
    url(r'^mpesa/', views.mpesa_gateway, name='mpesa_gateway'),
    url(r'^new_user.', views.index_page, name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),


]
