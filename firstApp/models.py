from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}" 