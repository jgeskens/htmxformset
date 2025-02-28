from django.db import models


class TodoItem(models.Model):
    description = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    done = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'- [{self.done and "x" or " "}] {self.description}'
