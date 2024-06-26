# Generated by Django 3.2.11 on 2024-05-29 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20240529_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='batch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='p_img'),
        ),
    ]
