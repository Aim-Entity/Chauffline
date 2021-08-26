from django.db import models


class Testimonials(models.Model):
    message = models.CharField(max_length=250)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'testimonials'
        # Add verbose name
        verbose_name = 'Testimonial'
