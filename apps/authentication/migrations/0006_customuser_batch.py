# Generated by Django 3.2.11 on 2024-05-29 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_customuser_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='batch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]