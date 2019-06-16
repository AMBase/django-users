from django.urls import path
from .views import IndexView, SignInView, SignUpView 

app_name = 'users'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sign-in', SignInView.as_view(), name='sign_in'),
    path('sign-up', SignUpView.as_view(), name='sign_up'),
]