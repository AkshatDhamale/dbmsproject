# Generated by Django 3.2 on 2021-05-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0010_remove_registerperson_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerperson',
            name='Person_DOB',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='registerperson',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registerperson',
            name='nationality',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registerperson',
            name='phonenumber',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='registerperson',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
