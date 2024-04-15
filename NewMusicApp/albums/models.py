from django.core.exceptions import ValidationError
from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    GENRE_CHOICES = [
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other")
    ]
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    image_url = models.URLField()
    price = models.FloatField()

    def clean(self):
        if self.price < 0.0:
            raise ValidationError("Price cannot be below 0.0.")
