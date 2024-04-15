# In views.py of profiles app
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, DeleteView, CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm
from .models import Profile
from ..albums.models import Album


class CreateProfileView(CreateView):
    template_name = 'web/home-no-profile.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()
        return redirect('web/home-with-profile')  # Redirect to home page after profile creation

class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'  # Specify the template name

    def get_object(self, queryset=None):
        # Fetch the profile based on some predefined logic
        # For example, you could fetch the first profile in the database
        return Profile.objects.first()




def delete_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.first()
        profile.delete()
        Album.objects.all().delete()
        return redirect('index')
    return render(request, 'profiles/profile-delete.html')
