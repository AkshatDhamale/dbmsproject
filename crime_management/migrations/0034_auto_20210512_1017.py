# Generated by Django 3.2 on 2021-05-12 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0033_chargesheet_report_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigation_report',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='investigation_report',
            name='main_suspect_DOB',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='investigation_report',
            name='main_suspect_address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investigation_report',
            name='main_suspect_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investigation_report',
            name='main_suspect_phone_no',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='investigation_report',
            name='main_witness_DOB',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='investigation_report',
            name='main_witness_address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investigation_report',
            name='main_witness_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investigation_report',
            name='main_witness_phone_no',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='investigation_report',
            name='scene_firstvisited',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]