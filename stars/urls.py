from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('rate-image/', rate_image, name='rate')
]