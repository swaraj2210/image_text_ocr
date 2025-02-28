from django.urls import path
from .views import home, extract_text

urlpatterns = [
    path('', home, name='home'),
    path('extract/', extract_text, name='extract_text'),
]
