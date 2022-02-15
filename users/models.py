from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage as storage

# Extending User Model Using a One-To-One Link
from django.urls import reverse_lazy


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='media/default.jpg', upload_to='profile_images/%Y/%m')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
