from django.urls import path
from .views import ProfileDetailsView
from ..profiles import views

urlpatterns = [
    path('details/', ProfileDetailsView.as_view(), name='profile_details'),
    path('delete/', views.delete_profile, name='delete_profile'),
]


