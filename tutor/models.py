from django.db import models

from .validators import title_val

class Post(models.Model):
    title = models.CharField(max_length=20, 
        validators=[title_val])
    body = models.TextField()
    email = models.EmailField(blank=True)

    def __str__(self):
        return "{}".format(self.title)
        