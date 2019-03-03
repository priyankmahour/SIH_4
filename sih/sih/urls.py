"""sih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from testapp import views

from rest_framework_jwt.views  import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/$',views.User_details_CR.as_view(),name="User_details_CR"),
    url(r'^user/(?P<pk>\d+)/$',views.User_details_UD.as_view(),name="User_details_UD"),
    # url(r'^u_login/$',views.User_login_details_CR.as_view(),name="User_login_details_CR"),
    # url(r'^u_login/(?P<pk>\d+)/$',views.User_login_details_UD.as_view(),name="User_login_details_UD"),
    url(r'^location/$',views.User_location_details_CR.as_view(),name="User_location_details_CR"),
    url(r'^location/(?P<pk>\d+)/$',views.User_location_details_UD.as_view(),name="User_location_details_UD"),
    url(r'^driver/$',views.Driver_details_CR.as_view(),name="Driver_details_CR"),
    url(r'^driver/(?P<pk>\d+)/$',views.Driver_details_UD.as_view(),name="Driver_details_UD"),
    url(r'^d_loc/$',views.Driver_location_details_CR.as_view(),name="Driver_location_details_CR"),
    url(r'^d_loc/(?P<pk>\d+)/$',views.Driver_location_details_UD.as_view(),name="Driver_location_details_UD"),
    url(r'^booking/$',views.Booking_CR.as_view(),name="Booking_CR"),
    url(r'^booking/(?P<pk>\d+)/$',views.Booking_UD.as_view(),name="Booking_UD"),
    url(r'^hospital/$',views.Hospital_details_CR.as_view(),name="Hospital_details_CR"),
    url(r'^hospital/(?P<pk>\d+)/$',views.Hospital_details_UD.as_view(),name="Hospital_details_UD"),


    # registring view for JWT Authentication .....
    url(r'^auth-jwt/',obtain_jwt_token,name="auth-jwt"),
    url(r'^auth-jwt-refresh/',refresh_jwt_token,name="auth-jwt-refresh"),
    url(r'^auth-jwt-verify/',verify_jwt_token,name="auth-jwt-verify"),
    url(r'^api/$',views.DistanceListAPIView.as_view(),name="DistanceListAPIView"),

]
