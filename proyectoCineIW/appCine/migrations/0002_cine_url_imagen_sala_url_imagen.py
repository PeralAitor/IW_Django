# Generated by Django 5.1.2 on 2024-10-31 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cine',
            name='url_imagen',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='url_imagen',
            field=models.URLField(blank=True, null=True),
        ),
    ]
