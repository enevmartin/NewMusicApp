from django.shortcuts import render, redirect

from NewMusicApp.albums.models import Album
from NewMusicApp.profiles.forms import RegistrationForm
from NewMusicApp.profiles.models import Profile


def home_page(request):
    try:
        profile = Profile.objects.all()[0]
        context = {
            'profile': profile,
            'albums': Album.objects.all(),
        }
        return render(request, 'web/home-with-profile.html', context=context)
    except IndexError:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            context = {'form': form}
            return render(request, 'web/home-no-profile.html', context)
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'web/home-no-profile.html', context)
