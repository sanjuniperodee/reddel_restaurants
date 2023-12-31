# Generated by Django 2.2 on 2023-09-21 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_certificate_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='encode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
