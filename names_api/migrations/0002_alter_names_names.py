# Generated by Django 4.2 on 2024-12-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='names',
            name='names',
            field=models.CharField(max_length=255),
        ),
    ]
