from django.db import models

class City_wheather(models.Model):
    city = models.CharField(max_length=30,primary_key=True)
    forcastday = models.SmallIntegerField()
    today = models.SmallIntegerField()
    day_1 = models.SmallIntegerField()
    day_2 = models.SmallIntegerField()
    day_3 = models.SmallIntegerField()
    day_4 = models.SmallIntegerField()
    day_5 = models.SmallIntegerField()
    day_6 = models.SmallIntegerField()
    day_7 = models.SmallIntegerField()

    def __str__(self):
        return self.city