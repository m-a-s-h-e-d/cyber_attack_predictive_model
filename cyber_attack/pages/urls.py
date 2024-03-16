# pages/urls.py
from django.urls import path
from .views import homePageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('homePost/', homePost, name='homePost'),
    path('results/<str:rst_count>/<str:urg_count>/<str:flow_duration>/<str:duration>/<str:weight>/<str:variance>', results, name='results'),
]