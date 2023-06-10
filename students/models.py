from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=100, default=user)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    roll_num = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.name
