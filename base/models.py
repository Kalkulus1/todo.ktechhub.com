from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")
        ordering = ['complete']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Task_detail", kwargs={"pk": self.pk})

