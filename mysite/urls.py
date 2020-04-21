from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('register/', views.register),
    path('login/', views.logging),
    path('myProfile/', views.my_profile),
    path('addPhoto/', views.add_photo),
    path('logout/', views.logout_view),
    path('photo/<int:photo_id>/', views.get_photo),
]
