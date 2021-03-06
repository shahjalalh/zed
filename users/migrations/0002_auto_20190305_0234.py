# Generated by Django 2.1.7 on 2019-03-05 02:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lat',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitude'),
        ),
        migrations.AddField(
            model_name='user',
            name='lon',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='user',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='user',
            name='portfolio_site',
            field=models.URLField(blank=True, null=True, verbose_name='Portfolio Site'),
        ),
    ]
