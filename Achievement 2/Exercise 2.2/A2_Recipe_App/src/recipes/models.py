from django.db import models

difficulty_choices = (('easy', 'Easy'), ('medium', 'Medium'),
                      ('intermediate', 'Intermediate'), ('hard', 'Hard'))


class Recipes(models.Model):
    # username = models.OneToOneField(User, on_delete=models .CASCADE)
    name = models.CharField(max_length=120)
    # image will be added later
    adapted = models.CharField(max_length=120)
    adapted_link = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    direction = models.CharField(max_length=10000)
    prepTime = models.PositiveIntegerField()
    cookTime = models.PositiveIntegerField()
    totalTime = models.PositiveIntegerField()
    serving = models.PositiveIntegerField()
    difficulty = models.CharField(
        max_length=12, choices=difficulty_choices, default='easy')
    ingredients = models.CharField(max_length=1000)

    def __str__(self):
        return (str(self.name))
