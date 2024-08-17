from django.db import models


class HikeUser(models.Model):
    email = models.CharField(max_length=50)
    fam = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    otc = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)

class Coords(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    height = models.IntegerField(null=True)


class Level(models.Model):
    LEVEL = [
        ('1А', '1А'),
        ('2А', '2А'),
        ('3А', '3А'),
        ('1B', '1Б'),
        ('2B', '2Б'),
        ('3B', '3Б'),
        ('3B*', '3Б*'),
    ]

    winter = models.CharField(max_length=3, choices=LEVEL, blank=True)
    summer = models.CharField(max_length=3, choices=LEVEL, blank=True)
    autumn = models.CharField(max_length=3, choices=LEVEL, blank=True)
    spring = models.CharField(max_length=3, choices=LEVEL, blank=True)


class Pereval(models.Model):

    STATUSES = [
        ('new', 'Новое'),
        ('pen', 'На рассмотрении'),
        ('acp', 'Принято'),
        ('rej', 'Отклонено'),
    ]

    beauty_title = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50)
    other_titles = models.CharField(max_length=128, blank=True)
    connect = models.CharField(max_length=128, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(HikeUser, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUSES, default='new')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Image(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, blank=True, related_name='images')
    title = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)