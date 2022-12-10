from django.db import models
from django.contrib.auth import get_user_model
from urlshourter.url_maker import make_short_url

User = get_user_model()


# Create your models here.


class UrlModel(models.Model):
    code = models.CharField(max_length=220, primary_key=True, blank=True)
    long_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='url_maker', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = make_short_url()
        super().save(*args, **kwargs)
