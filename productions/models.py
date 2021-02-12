from django.db import models

class Productions(models.Model):
    year = models.IntegerField()
    productionType = models.CharField(max_length=30)
    file = models.FileField('Excel File', upload_to='files/', max_length=100)

