from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import urllib.request


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(blank=True, upload_to='profile_images/%Y/%m')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # # resizing images
    # def save(self, *args, **kwargs):
    #     return
    #     urllib.request.urlretrieve(self.avatar.url, "image.png")
    #     img = Image.open("image.png")
    #     if img.height > 100 or img.width > 100:
    #         new_img = (100, 100)
    #         img.thumbnail(new_img)
