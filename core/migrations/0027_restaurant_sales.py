# Generated by Django 2.2 on 2023-10-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20231002_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='sales',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
