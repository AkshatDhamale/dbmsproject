# Generated by Django 3.2 on 2021-05-08 05:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0005_alter_chargesheet_charging_officer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_Act',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_email',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_image',
            field=models.FileField(blank=True, default=None, max_length=255, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_phone_no',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_section',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('Oth', 'Other')], default='M', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_typeofoffense',
            field=models.CharField(blank=True, choices=[('SO', 'Summary offense'), ('IO', 'Indictable offense')], default='SO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Accused_underwhatlaw',
            field=models.CharField(blank=True, choices=[('State', 'State'), ('Act', 'Act'), ('Cwealth', 'CWealth'), ('Reg', 'Reg'), ('Other', 'Other')], default='State', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Assisting_officer',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Informant_address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Informant_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Informant_image',
            field=models.FileField(blank=True, default=None, max_length=255, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Informant_initial_report',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Informant_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Informant_phone_no',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Informant_signature',
            field=models.FileField(blank=True, default=None, max_length=255, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Investigation_details',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Investigation_officer',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Issued_at',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Issued_when',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Reporting_officer',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Suspects',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Theories',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='Witnesses',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='chargesheet',
            name='charging_officer',
            field=models.CharField(blank=True, default='username', max_length=255, null=True),
        ),
    ]
