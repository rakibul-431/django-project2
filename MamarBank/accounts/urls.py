
from django.urls import path
from accounts.views import UserRejistrationView
# from accounts import views

urlpatterns = [
    path('SignupPage/',UserRejistrationView.as_view(),name='Rejistar'),
]
