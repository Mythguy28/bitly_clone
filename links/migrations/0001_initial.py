# Generated by Django 5.0.6 on 2024-07-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('url', models.URLField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('clicks', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]
