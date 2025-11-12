from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Good(models.Model):
    manufacturers_list = []
    ipses_list = []

    title = models.CharField(max_length=255, default="Some Piece of Scrap")
    description = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    manufacturer = models.CharField(max_length=20, default=None)
    posted_at = models.DateField(default=timezone.now)
    main_picture = models.URLField()
    pictures_list = models.JSONField(default=list, blank=True)
    hover_picture = models.URLField(blank=True, null=True)
    is_available = models.BooleanField()
    characteristics = models.JSONField(default={"IPS": '0"',
                                                "CPU": "",
                                                "RAM": "0GB",
                                                "SSD": "0GB"})
    tags = models.JSONField(default=list)
    reviews = models.JSONField(default=list, blank=True)

    def split_title(self):
        if len(self.title) < 30:
            return self.title
        else:
            words = self.title.split()
            lines = []
            current = ""
            for word in words:
                if len(current + word + " ") < 30:
                    current += word + " "
                else:
                    lines.append(current)
                    current = word + " "
            if current:
                lines.append(current)
            return "\n".join(lines)
        
    def save(self, *args, **kwargs):
        if not self.hover_picture:
            self.hover_picture = self.main_picture
        super().save(*args, **kwargs)

        if self.manufacturer not in Good.manufacturers_list:
            Good.manufacturers_list.append(self.manufacturer)

        if int(self.characteristics['IPS'][0:2]) not in Good.ipses_list:
            Good.ipses_list.append(int(self.characteristics['IPS'][0:2]))
        
    def __str__(self):
        return self.title
    



class Review(models.Model):
    author = models.CharField(max_length=20)
    text = models.CharField(max_length=255)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    