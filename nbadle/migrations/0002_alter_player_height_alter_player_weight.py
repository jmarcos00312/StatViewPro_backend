# Generated by Django 4.2.3 on 2023-07-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbadle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.CharField(max_length=10),
        ),
    ]
