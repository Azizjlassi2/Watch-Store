# Generated by Django 4.0.5 on 2022-10-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('price', models.FloatField()),
                ('marque', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
