# Generated by Django 2.2.2 on 2019-09-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0013_auto_20190918_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingpostdevelopment',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='listingpostdevelopment',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=15, null=True),
        ),
    ]