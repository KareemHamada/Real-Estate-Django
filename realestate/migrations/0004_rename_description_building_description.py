# Generated by Django 4.0.2 on 2022-03-02 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0003_alter_building_bathroom_alter_building_rooms_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='Description',
            new_name='description',
        ),
    ]
