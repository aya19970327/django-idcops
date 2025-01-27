# Generated by Django 2.1.15 on 2021-10-25 09:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idcops', '0003_auto_20211014_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, help_text='设备高度(U)', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='设备高度(U)'),
        ),
    ]
