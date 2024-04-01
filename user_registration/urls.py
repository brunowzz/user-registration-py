from django.contrib import admin
from django.urls import path
from app_user_registration import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', views.users, name="user_list")
]
