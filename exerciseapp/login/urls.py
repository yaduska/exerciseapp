from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import logout_view,signup

app_name='login'
urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='login/login.html',authentication_form=LoginForm),name='login'),
    path('logout',logout_view,name='logout'),
    path('signup/',signup,name='signup'),
]


