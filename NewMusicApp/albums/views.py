# In views.py of albums app
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from .forms import AddAlbumForm, DisabledAddAlbumForm


class AddAlbumView(CreateView):
    model = Album
    form_class = AddAlbumForm
    template_name = 'albums/add-album.html'
    success_url = '/'  # Redirect to home page after successful album creation


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'albums/album-details.html'


class EditAlbumView(UpdateView):
    model = Album
    form_class = AddAlbumForm
    template_name = 'albums/edit-album.html'
    success_url = '/'  # Redirect to home page after successful album edit


class DeleteAlbumView(DeleteView):
    model = Album
    success_url = reverse_lazy('index')  # Redirect to home page after successful album deletion
    template_name = 'albums/delete-album.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Use the disabled form for rendering
        context['form'] = DisabledAddAlbumForm(instance=self.object)
        return context
