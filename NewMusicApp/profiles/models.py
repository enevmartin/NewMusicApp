from django.db import models
from django.core.exceptions import ValidationError

class Profile(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField(blank=True, null=True)

    def clean(self):
        if not (2 <= len(self.username) <= 15 and self.username.replace('_', '').isalnum()):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
        if self.age is not None and self.age < 0:
            raise ValidationError("Age cannot be below 0.")

