# Generated by Django 4.2.9 on 2024-01-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-06-23'),
            preserve_default=False,
        ),
    ]
