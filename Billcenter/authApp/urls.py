from django.urls import path
from .import views

app_name = 'auth'

urlpatterns = [
    path('auth/login', views.user_login, name="login"),  # Renamed view
    path('auth/signup', views.signup, name="signup"),
    path('verification/<str:email>/', views.email_verification, name="verify_email"),
    path('verify_otp/', views.verify_otp, name="verify_otp"),
    path('resend_otp/', views.resend_otp, name="resend_otp"),  # Added this line
    path('logout/', views.logout_view, name="logout"), 
]
