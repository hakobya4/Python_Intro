from django.db import models


class Users(models.Model):
    # username = models.OneToOneField(User, on_delete=models .CASCADE)
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    def __str__(self):
        return (str(self.name))
