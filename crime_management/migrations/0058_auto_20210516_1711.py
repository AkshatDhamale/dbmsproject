# Generated by Django 3.2 on 2021-05-16 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0057_auto_20210516_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('criminal_id', models.IntegerField(blank=True, default=None, null=True)),
                ('doctor_id', models.IntegerField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('previous_diseasesheight', models.IntegerField(blank=True, default=0, null=True)),
                ('family_diseases', models.TextField(blank=True, default=None, null=True)),
                ('allergies', models.TextField(blank=True, default=None, null=True)),
                ('current_medications', models.TextField(blank=True, default=None, null=True)),
                ('current_diseases', models.TextField(blank=True, default=None, null=True)),
                ('height', models.IntegerField(blank=True, default=0, null=True)),
                ('weight', models.IntegerField(blank=True, default=0, null=True)),
                ('BMI', models.IntegerField(blank=True, default=0, null=True)),
                ('BP', models.IntegerField(blank=True, default=0, null=True)),
                ('x_ray_results', models.TextField(blank=True, default=None, null=True)),
                ('x_ray_report', models.FileField(blank=True, default=None, max_length=255, null=True, upload_to='')),
                ('mental_report', models.TextField(blank=True, default=None, null=True)),
                ('Hearing', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('Vision', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('Dental', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('signature', models.FileField(blank=True, default=None, max_length=255, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='criminal',
            name='status_health_record',
            field=models.CharField(blank=True, choices=[('Uploaded', 'Uploaded'), ('Not_Uploaded', 'Not_Uploaded')], default='Not_Uploaded', max_length=255, null=True),
        ),
    ]
