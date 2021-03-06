# Generated by Django 3.2.5 on 2021-08-16 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CarHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('car_number', models.CharField(max_length=20)),
                ('come_time', models.DateTimeField()),
                ('go_time', models.DateTimeField()),
                ('sum', models.FloatField()),
                ('all_time', models.FloatField()),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.price')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('car_number', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.price')),
            ],
        ),
    ]
