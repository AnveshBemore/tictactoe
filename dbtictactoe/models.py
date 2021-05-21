from django.db import models

# Create your models here.
class Score(models.Model):
    Sno=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=200)
    Won=models.BooleanField(default=False)
    Lost=models.BooleanField(default=False)