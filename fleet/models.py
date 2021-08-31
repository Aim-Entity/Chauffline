from django.db import models

CATEGORY_CHOICES = (
    ("First Class", "First Class"),
    ("Executive", "Executive"),
    ("Business", "Business"),
    ("XL", "XL"),
)


class Car(models.Model):
    thumbnail = models.ImageField(upload_to="car_thumbnails")

    cover = models.ImageField(upload_to="car_covers")
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)

    quality_one = models.CharField(
        max_length=100, default="Passenger: 4", blank=True)
    quality_two = models.CharField(
        max_length=100, default="Luggages: 2", blank=True)

    decription = models.TextField()

    hourly_rate = models.IntegerField(default=50)
    daily_rate = models.IntegerField(default=350)

    slug = models.SlugField(
        default="please-input-in-this-format", max_length=100)

    def __str__(self):
        return f"{self.name}, {self.category}"
