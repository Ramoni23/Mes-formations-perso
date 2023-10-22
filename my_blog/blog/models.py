from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=120)
    updated_at = models.DateTimeField(auto_now=True) # date d'ajout

    # ordonner la date du plus recent au plus ancien
    class Meta:
        ordering = ["-updated_at"]

class Article(models.Model):
    title = models.CharField(max_length=150)
    Price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categorie")
    desc=models.TextField()
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    # ordonner la date du plus recent au plus ancien
    class Meta:
        ordering = ["-updated_at"]

    # def __str__(self):
        # return self.title # affiche que le titre de l'article dans l'espace admin