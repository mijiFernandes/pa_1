from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import urllib.request


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='media/default.jpg', upload_to='profile_images/%Y/%m')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()
        urllib.request.urlretrieve(self.avatar.url, "image.png")
        image = Image.open("image.png")
        resized_image = image.resize((100, 100), Image.ANTIALIAS)
        resized_image.save("image.png")
