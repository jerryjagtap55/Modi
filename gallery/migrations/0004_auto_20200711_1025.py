# Generated by Django 3.0.8 on 2020-07-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_photo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
