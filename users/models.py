
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    # Override to prevent DRF from trying to inspect them
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        blank=True
    )

    def __str__(self):
        return self.username



class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"
