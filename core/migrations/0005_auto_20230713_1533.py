# Generated by Django 2.2 on 2023-07-13 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230710_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='encode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Color'),
        ),
        migrations.AlterField(
            model_name='color',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='item',
            name='color',
        ),
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, to='core.Color'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='session_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
