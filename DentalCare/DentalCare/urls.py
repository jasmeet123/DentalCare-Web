"""DentalCare URL Configuration

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
from django.contrib import admin
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from UserRequest.views import UserRequest
from UserLogin.views import FacebookLoginOrSignup
from rest_framework.authtoken import views
from Tips.views import TipViewSet
from Tips.views import TipTodayList
from UserLogin.views import UserLogout
from dentist_login.views import DentistView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^dentist/$',csrf_exempt(DentistView.as_view()), name = "dentist"),
    url(r'^tips/$', csrf_exempt(TipViewSet.as_view())),
    url(r'^request/$',csrf_exempt(UserRequest.as_view()), name = "request"),
    url(r'^logout/$',csrf_exempt(UserLogout.as_view()), name = "logout"),
    url(r'^facebook-signup/$', csrf_exempt(FacebookLoginOrSignup.as_view()), name='facebook-signup'),
    url(r'^facebook-signup/(?P<pk>\d+)/$', csrf_exempt(FacebookLoginOrSignup.as_view()), name='facebook-signup'),
    url(r'^tips/(?P<date>(\d{4}-\d{2}-\d{2}))/$', TipTodayList.as_view(),name='tiplist'),
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



