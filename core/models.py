from django.core.checks import messages
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.http import request
from django.shortcuts import reverse, get_object_or_404, redirect
from django.utils import timezone
from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)
    image = models.ImageField(default=None)


class Certificate(models.Model):
    sum = models.FloatField()
    user_id = models.CharField(max_length=255, null=True, blank=True)
    encode = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=False, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Restaurant(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    tags = models.ManyToManyField(Tag, default=None)
    average = models.CharField(max_length=255, null=True)
    food_type = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    menu = models.ImageField(null=True)
    sale = models.ImageField(null=True)
    prices = models.CharField(null=True, max_length=255)
    slug = models.SlugField(null=True)
    location = models.CharField(max_length=255, null=True)
    kitchen = models.CharField(max_length=255, null=True)
    novy = models.BooleanField(default=False)


    def __str__(self):
        return self.title


class RestaurantImage(models.Model):
    post = models.ForeignKey(Restaurant, default=None, on_delete=models.CASCADE)
    images = models.ImageField()
    def __str__(self):
        return self.post.title


class Favorites(models.Model):
    user = models.CharField(max_length=255)
    restaurants = models.ManyToManyField(Restaurant, default=None)

def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
