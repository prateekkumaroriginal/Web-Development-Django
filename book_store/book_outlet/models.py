from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city} - {self.zip_code}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = ("Countries")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    published_countries = models.ManyToManyField(Country, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"
