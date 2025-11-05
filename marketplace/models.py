from django.db import models
from django.utils import timezone


# Create your models here.

class Good(models.Model):
    title = models.CharField(max_length=255, default="Some Piece of Scrap")
    description = models.CharField(max_length=500, default=title)
    price = models.IntegerField()
    posted_at = models.DateField(default=timezone.now)
    main_picture = models.URLField()
    hover_picture = models.URLField(default=main_picture)
    pictures_list = models.JSONField(default=list)
    is_available = models.BooleanField()
    reviews_qty = models.IntegerField()