# Generated by Django 2.2 on 2023-09-22 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20230923_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='otkliki',
            field=models.ManyToManyField(default=None, null=True, to='core.Otklik'),
        ),
    ]
