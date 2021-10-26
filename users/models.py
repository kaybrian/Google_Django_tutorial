from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.CharField(
        verbose_name='Address', max_length=100, null=True, blank=True)
    town = models.CharField(verbose_name='town',
                            max_length=100, null=True, blank=True)
    country = models.CharField(
        verbose_name='country', max_length=100, null=True, blank=True)
    post_code = models.CharField(
        verbose_name='post', max_length=8, null=True, blank=True)
    country = models.CharField(
        verbose_name='country', max_length=100, null=True, blank=True)
    longitude = models.CharField(
        verbose_name='longitude', max_length=100, null=True, blank=True)
    latitude = models.CharField(
        verbose_name='latitude', max_length=100, null=True, blank=True)

    captcha_score = models.FloatField(default=0.0)
    has_profile = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user
