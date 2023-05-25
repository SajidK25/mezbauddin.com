from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns...
    path('', views.home, name='home'),
	# New URL patterns...
]
