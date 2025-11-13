from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class SavedCharacteristics(models.Model):
    ipses = models.JSONField(default=list, blank=True)
    cpus = models.JSONField(default=list, blank=True)
    rams = models.JSONField(default=list, blank=True)
    ssds = models.JSONField(default=list, blank=True)
    manufacturers = models.JSONField(default=list, blank=True)

class Good(models.Model):
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

        if int(self.characteristics['IPS'][0:2]) not in saved_chars.ipses:
            saved_chars.ipses.append(int(self.characteristics['IPS'][0:2]))
        
        cpu = self.characteristics['CPU']
        if cpu not in saved_chars.cpus:
            saved_chars.cpus.append(cpu)

        ram = self.characteristics['RAM']
        if ram not in saved_chars.rams:
            saved_chars.rams.append(ram)

        ssd = self.characteristics['SSD']
        if ssd not in saved_chars.ssds:
            saved_chars.ssds.append(ssd)

        saved_chars.save()


    def __str__(self):
        return self.title



class Review(models.Model):
    author = models.CharField(max_length=20)
    text = models.CharField(max_length=255)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    