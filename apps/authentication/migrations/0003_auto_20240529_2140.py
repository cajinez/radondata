# Generated by Django 3.2.11 on 2024-05-29 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20240529_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='batch',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
