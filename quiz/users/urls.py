from django.urls import path
from .views import home, RegisterView

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
]

