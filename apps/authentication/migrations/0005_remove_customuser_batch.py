# Generated by Django 3.2.11 on 2024-05-29 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20240529_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='batch',
        ),
    ]
