# Generated by Django 5.0.1 on 2024-01-26 16:51

import django.db.models.deletion
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
                ('name', models.CharField(max_length=255)),
                ('times_prepared', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.product')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(through='product_app.RecipeProduct', to='product_app.product'),
        ),
    ]
