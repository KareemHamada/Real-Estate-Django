# Generated by Django 4.0.2 on 2022-04-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_rename_rooms_number_building_rooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='photos',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='building',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='building',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='building',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='building',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
