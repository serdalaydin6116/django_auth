from django.urls import path
from .views import home_view, special, register 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name="home"),
    path('special', special, name="special"),
    path('register', register, name="register"),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change_password.html'), name="change_password"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'registration/reset_password.html'), name="reset_password"),
]