# Generated by Django 4.2.4 on 2023-09-04 10:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_app', '0002_musician_salary_alter_musician_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='salary',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
