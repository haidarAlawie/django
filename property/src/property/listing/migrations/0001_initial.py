# Generated by Django 2.2.2 on 2019-06-21 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingPostDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True)),
                ('first_line_address', models.CharField(max_length=50, null=True)),
                ('second_line_address', models.CharField(blank=True, max_length=50, null=True)),
                ('postcode', models.CharField(max_length=12, null=True)),
                ('number_of_properties', models.IntegerField(null=True)),
                ('site_plan', models.IntegerField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('ownership', models.CharField(max_length=50, null=True)),
                ('tenure', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]