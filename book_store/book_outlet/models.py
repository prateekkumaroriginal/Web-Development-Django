from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MaxLengthValidator(5), MinLengthValidator(1)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    

    def __str__(self):
        return f"{self.title} ({self.rating})"
