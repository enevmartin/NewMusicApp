from django.urls import path
from .views import (
    AddAlbumView, AlbumDetailsView, EditAlbumView, DeleteAlbumView
)

urlpatterns = [
    path('add/', AddAlbumView.as_view(), name='add_album'),
    path('details/<int:pk>/', AlbumDetailsView.as_view(), name='album_details'),
    path('edit/<int:pk>/', EditAlbumView.as_view(), name='edit_album'),
    path('delete/<int:pk>/', DeleteAlbumView.as_view(), name='delete_album'),
]
