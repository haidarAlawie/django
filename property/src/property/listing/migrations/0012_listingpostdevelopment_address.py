# Generated by Django 2.2.2 on 2019-09-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0011_remove_listingpostdevelopment_daee'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingpostdevelopment',
            name='address',
            field=models.TextField(null=True),
        ),
    ]