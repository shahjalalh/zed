# Generated by Django 2.1.7 on 2019-03-06 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190306_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Profession'),
        ),
    ]
