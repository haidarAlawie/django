# Generated by Django 2.2.2 on 2019-09-18 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0010_auto_20190918_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingpostdevelopment',
            name='daee',
        ),
    ]