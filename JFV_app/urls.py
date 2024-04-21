from django.contrib import admin
from django.urls import path, include
from .views.h_views import show_top

from .views import finance_chart

urlpatterns = [
    path('top', show_top),
    path('chart', finance_chart),
]
