# Generated by Django 4.0.2 on 2022-03-01 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='bathroom',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='building',
            name='forwhat',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='building',
            name='rooms_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='building',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
