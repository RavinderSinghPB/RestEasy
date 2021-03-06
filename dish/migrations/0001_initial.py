# Generated by Django 3.2.3 on 2021-05-14 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('calorie', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DishDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('speciality', models.CharField(blank=True, max_length=255)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dish.dish')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.restaurant')),
            ],
        ),
    ]
