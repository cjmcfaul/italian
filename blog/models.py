from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpResponseRedirect


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    published = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    rating_info = models.ForeignKey(
        'blog.rating',
        on_delete=models.CASCADE,
    )
    image_one = models.ImageField(
        upload_to='static/blog/media/uploads',
        default = '/None/no-img.jpg')

    def __unicode__(self):
        return '%s' % self.title


class Rating(models.Model):
    sandwich_name = models.CharField(max_length=300, null = True)
    bread_quality = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10),], null = True)
    meat_quality = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10),], null = True)
    meat_quantity = models.PositiveIntegerField(default=0,  validators=[MaxValueValidator(10),],null = True)
    veg_quality = models.PositiveIntegerField(default=0,  validators=[MaxValueValidator(10),],null = True)
    veg_quantity = models.PositiveIntegerField(default=0,  validators=[MaxValueValidator(10),],null = True)
    dressing_quality = models.PositiveIntegerField(default=0,  validators=[MaxValueValidator(10),],null = True)
    dressing_quantity = models.PositiveIntegerField(default=0,  validators=[MaxValueValidator(10),],null = True)

    def __unicode__(self):
        return '%s' % self.sandwich_name

    def score(self):
        b_ql = int(self.bread_quality)
        m_ql = int(self.meat_quality)
        m_qt = int(self.meat_quantity)
        v_ql = int(self.veg_quality)
        v_qt = int(self.veg_quantity)
        d_ql = int(self.dressing_quality)
        d_qt = int(self.dressing_quantity)

        total = b_ql + m_ql + m_qt + v_ql + v_qt + d_ql + d_qt

        return total


class Restaurant(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
    )
    address = models.CharField(max_length=500, null = True)
    website = models.CharField(max_length=200, null = True)
    phone_number = models.CharField(max_length=12, null = True)
    email = models.CharField(max_length=75, null = True)
    rating_info = models.ForeignKey(
        'blog.rating',
        on_delete=models.CASCADE,
        null=True,
        blank = True,
    )
    latitude = models.IntegerField(
        blank=True,
        null=True,
    )
    longitude = models.IntegerField(
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return '%s' % self.name

    def get_lat_long(self):
        from googlemaps import GoogleMaps
        gmaps = GoogleMaps(italian-1489414695369)
        Address = self.address
        lat, lng = gmaps.address_to_latlng(address)
        self.latitude = lat
        self.longitude = lng
        save()
