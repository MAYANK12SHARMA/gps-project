# Generated by Django 5.0.6 on 2024-06-20 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPS_Toll_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='date_entered',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
