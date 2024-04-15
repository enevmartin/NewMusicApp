# In forms.py of albums app

# In forms.py of albums app

from django import forms

from .models import Album


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'genre', 'description', 'image_url', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }

class DisabledAddAlbumForm(AddAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True

