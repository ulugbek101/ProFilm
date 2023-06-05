from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default="1", verbose_name="Who owns that film ?")
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="film-photos/", null=True)
    description = models.TextField()
    trailer_link = models.URLField(null=True, verbose_name="Youtube link")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
