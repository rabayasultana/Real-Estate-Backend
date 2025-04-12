# Generated by Django 5.2 on 2025-04-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_title', models.CharField()),
                ('image', models.URLField()),
                ('segment_name', models.CharField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('status', models.CharField()),
                ('area', models.CharField()),
                ('location', models.CharField()),
                ('facilities', models.JSONField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]
