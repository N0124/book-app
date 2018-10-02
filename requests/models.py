from django.db import models


class Request(models.Model):
    path = models.CharField(max_length=1000)
    method = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.method} {self.path}'
