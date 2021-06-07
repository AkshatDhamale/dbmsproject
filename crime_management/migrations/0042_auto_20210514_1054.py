# Generated by Django 3.2 on 2021-05-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0041_case_def_crime_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chargesheet',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=255, null=True),
        ),
    ]
