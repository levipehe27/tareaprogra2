from django.urls import path
from .views import analizar

urlpatterns = [
    path('texto', analizar ),
]
