# Generated by Django 4.2.5 on 2023-09-08 15:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('student_id', models.CharField(max_length=13, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(13)])),
                ('name', models.CharField(max_length=55)),
                ('solve1', models.DecimalField(decimal_places=3, max_digits=7)),
                ('solve2', models.DecimalField(decimal_places=3, max_digits=7)),
                ('solve3', models.DecimalField(decimal_places=3, max_digits=7)),
                ('solve4', models.DecimalField(decimal_places=3, max_digits=7)),
                ('solve5', models.DecimalField(decimal_places=3, max_digits=7)),
                ('solve_best', models.DecimalField(decimal_places=3, max_digits=7)),
                ('solve_avg', models.DecimalField(decimal_places=3, max_digits=7)),
            ],
        ),
    ]
