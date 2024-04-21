from django.contrib import admin
from django.urls import path, include
from .views.views.py import show_top


urlpatterns = [
    path('admin/', admin.site.urls),
    path('top', show_top),
]
