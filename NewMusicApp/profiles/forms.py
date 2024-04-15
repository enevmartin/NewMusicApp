# In forms.py

from django import forms

from django import forms
from .models import Profile

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    age = forms.IntegerField(label="Age", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Age'}))

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

