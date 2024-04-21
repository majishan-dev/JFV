from django.contrib import admin
from django.urls import path, include
from .views.h_views import show_top, show_test

from .views import finance_chart

urlpatterns = [
    path('top', show_top),
    path('test', show_test),
    path('chart', finance_chart),
]
