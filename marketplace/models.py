from django.db import models
from django.utils import timezone


# Create your models here.

class Good(models.Model):
    title = models.CharField(max_length=255, default="Some Piece of Scrap")
    description = models.CharField(max_length=500, default=title.name)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=20, default=None)
    posted_at = models.DateField(default=timezone.now)
    main_picture = models.URLField()
    hover_picture = models.URLField(default=main_picture)
    pictures_list = models.JSONField(default=list)
    is_available = models.BooleanField()
    reviews_qty = models.IntegerField()
    characteristics = models.JSONField(default=dict)
    tags = models.JSONField(default=list)