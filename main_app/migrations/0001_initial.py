# Generated by Django 4.1.3 on 2022-11-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(max_length=4)),
                ('color', models.CharField(max_length=100)),
                ('kms', models.IntegerField(max_length=15)),
                ('trans', models.CharField(max_length=100)),
            ],
        ),
    ]
