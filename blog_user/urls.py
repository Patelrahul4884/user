from django.urls import path
from .views import UserCreateView, LoginView, test,get_token

urlpatterns = [
    path('user_create/',UserCreateView.as_view()),
    path('user_login/', LoginView.as_view()),
    path('test/', test.as_view()),
    path('get_token/',get_token.as_view())
]