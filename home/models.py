from django.db import models
from fleet.models import Car


class Testimonials(models.Model):
    message = models.CharField(max_length=250)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'testimonials'
        # Add verbose name
        verbose_name = 'Testimonial'


class PopularCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            related_name="popular_car")

    def __str__(self):
        return self.car.name
