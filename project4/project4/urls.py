
from django.contrib import admin
from django.urls import path,include
from . import views
from first_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',views.contact),
    path("",views.Home),
    path("first_app/",include("first_app.urls")),
]
