# Generated by Django 2.2.1 on 2019-05-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventCenter', '0003_auto_20190516_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
