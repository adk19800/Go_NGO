# Generated by Django 3.1.2 on 2020-11-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_registration_donate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='author',
        ),
        migrations.AddField(
            model_name='registration',
            name='amt_needed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='registration',
            name='amt_raised',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
