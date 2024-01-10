from django.db import models

class File(models.Model):
    prompt=models.CharField(max_length=1000)
    file=models.FileField(upload_to='file/')

    def __str__(self):
        return self.prompt