from django.urls import path
from .import views

app_name = 'dashboard'

urlpatterns = [
    path('user/', views.dashboard, name="home"),
    path('user/top-up', views.topup, name="topup"),
    path('user/top-up/mtn', views.topup_mtn, name="topup_mtn"),
    path('user/top-up/airtel', views.topup_airtel, name="topup_airtel"),
    path('user/top-up/glo', views.topup_glo, name="topup_glo"),
    path('user/top-up/9mobile', views.topup_9mobile, name="topup_9mobile"),
    path('user/electricity', views.electricity, name="electricity"),
    path('user/electricity/aedc', views.electricity_aedc, name="electricity_aedc"),
    path('user/tv', views.tv, name="tv"),
    path('user/tv/dstv', views.tv_dstv, name="tv_dstv"),
    path('user/tv/gotv', views.tv_gotv, name="tv_gotv"),
    path('user/tv/startimes', views.tv_startimes, name="tv_startimes"),
    path('user/travel', views.travel, name="travel"),
    path('user/travel/nigerian-air', views.travel_9jair, name="travel_9jair"),
    path('user/travel/nrc', views.travel_nrc, name="travel_nrc"),
    path('user/hotel', views.hotel, name="hotel"),
    path('user/hotel/sheraton', views.hotel_sheraton, name="hotel_sheraton"),
]