from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class SavedCharacteristics(models.Model):
    screen_diagonals = models.JSONField(default=list, blank=True)
    screen_refresh_rates = models.JSONField(default=list, blank=True)
    cpus = models.JSONField(default=list, blank=True)
    gpus = models.JSONField(default=list, blank=True)
    rams = models.JSONField(default=list, blank=True)
    storage_capacities = models.JSONField(default=list, blank=True)
    manufacturers = models.JSONField(default=list, blank=True)
    min_price = models.IntegerField(max_length=8, default=10000000)
    max_price = models.IntegerField(max_length=8, default=0)

class Good(models.Model):
    title = models.CharField(max_length=255, default="Some Piece of Scrap")
    description = models.CharField(max_length=500, blank=True)
    price = models.IntegerField(max_length=8)
    manufacturer = models.CharField(max_length=20, default=None)
    posted_at = models.DateField(default=timezone.now)
    main_picture = models.URLField()
    pictures_list = models.JSONField(default=list, blank=True)
    hover_picture = models.URLField(blank=True, null=True)
    is_available = models.BooleanField()
    screen_diagonal = models.CharField(max_length=10, default='0')
    screen_refresh_rate = models.CharField(max_length=10, default='0Hz')
    CPU = models.CharField(max_length=100, default='')
    GPU = models.CharField(max_length=100, default='')
    RAM = models.CharField(max_length=100, default='0GB')
    storage_capacity = models.CharField(max_length=100, default='0GB')
    tags = models.JSONField(default=list, blank=True)
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
                if len(lines) == 2:
                    return "\n".join(lines) + "..."
            if current:
                lines.append(current)
            return "\n".join(lines)
        
    def save(self, *args, **kwargs):
        if not self.hover_picture:
            self.hover_picture = self.main_picture

        super().save(*args, **kwargs)

        saved_chars, created = SavedCharacteristics.objects.get_or_create(id=1)

        if self.manufacturer and self.manufacturer not in saved_chars.manufacturers:
            saved_chars.manufacturers.append(self.manufacturer)

        # if len(self.characteristics['IPS']) > 2:
        #     self.characteristics['IPS'] = self.characteristics['IPS'][0:2]

        if len(self.screen_diagonal) > 3 :
            if self.screen_diagonal[2] == '.':
                if self.screen_diagonal[0:4] not in saved_chars.screen_diagonals:
                    saved_chars.screen_diagonals.append(self.screen_diagonal[0:4])

        elif self.screen_diagonal[0:2] not in saved_chars.screen_diagonals:
            saved_chars.screen_diagonals.append(self.screen_diagonal[0:2])
        
        if self.screen_refresh_rate not in saved_chars.screen_refresh_rates:
            saved_chars.screen_refresh_rates.append(self.screen_refresh_rate)

        if self.CPU not in saved_chars.cpus:
            saved_chars.cpus.append(self.CPU)


        if self.GPU not in saved_chars.gpus:
            saved_chars.gpus.append(self.GPU)


        if self.RAM not in saved_chars.rams:
            saved_chars.rams.append(self.RAM)


        if self.storage_capacity not in saved_chars.storage_capacities:
            saved_chars.storage_capacities.append(self.storage_capacity)


        if self.price < saved_chars.min_price:
            saved_chars.min_price = round(self.price)

        elif self.price > saved_chars.max_price:
            saved_chars.max_price = round(self.price)


        saved_chars.save()


    def __str__(self):
        return self.title



class Review(models.Model):
    author = models.CharField(max_length=20)
    text = models.CharField(max_length=255)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    