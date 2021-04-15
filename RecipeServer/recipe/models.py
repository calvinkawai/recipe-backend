from django.db import models

# Create your models here.
class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='recipe', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    ingredient = models.JSONField()
    steps = models.JSONField()
    image = models.ImageField(upload_to='image_folder/')

    class Meta:
        ordering = ['created']
