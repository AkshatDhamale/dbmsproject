# Generated by Django 3.2 on 2021-06-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0073_auto_20210602_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='case_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]