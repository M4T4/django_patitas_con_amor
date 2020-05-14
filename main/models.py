from django.db import models
from datetime import datetime

class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Da el plural correcto para el admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otros "Tutorial Seriess en admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
   #Se me presento un error con el default, en vez de default=1 lo cambie a lo que se ve.
    tutorial_slug = models.CharField(max_length=200, default=1)
# Este es el formato de datos para nuestra BD
    def __str__(self):
        return self.tutorial_title
