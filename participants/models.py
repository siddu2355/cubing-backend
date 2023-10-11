from django.db import models
from django.core.validators import MinLengthValidator


class Participant(models.Model):
    student_id = models.CharField(max_length=13, primary_key=True, validators=[MinLengthValidator(13)])
    name = models.CharField(max_length=55)
    competetion = models.CharField(max_length=55)
    solve1 = models.DecimalField(max_digits=7, decimal_places=3)
    solve2 = models.DecimalField(max_digits=7, decimal_places=3)
    solve3 = models.DecimalField(max_digits=7, decimal_places=3)
    solve4 = models.DecimalField(max_digits=7, decimal_places=3)
    solve5 = models.DecimalField(max_digits=7, decimal_places=3)
    solve_best = models.DecimalField(max_digits=7, decimal_places=3)
    solve_avg = models.DecimalField(max_digits=7, decimal_places=3)