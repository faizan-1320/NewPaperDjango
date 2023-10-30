from django.urls import path
from .views import SignUpView
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('singup/', SignUpView.as_view(), name='signup'),
    path('password-change/', views.PasswordChange, name='password-change'),
    path('password-done/', views.password_change_done, name='password-done'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='registration/custom_rest_password.html',html_email_template_name='registration/custom_password_reset_email.html')),
    path('password_reset/done/',auth_view.PasswordResetCompleteView.as_view(template_name='registration/custom_rest_done.html')),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='registration/custom_new_password.html')),
]