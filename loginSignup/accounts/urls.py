from django.urls import path
from .views import RegisterView,LoginView,accounts

urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('accounts/', accounts, name='accounts'),
]
