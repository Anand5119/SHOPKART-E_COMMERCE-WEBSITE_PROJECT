# Generated by Django 4.2.2 on 2023-08-01 19:10

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.getFilename)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.getFilename)),
                ('description', models.CharField(max_length=150)),
                ('rating', models.FloatField()),
                ('rating_count', models.IntegerField()),
                ('quantity', models.IntegerField(null=True)),
                ('offerPrice', models.IntegerField()),
                ('originalPrice', models.IntegerField()),
                ('priceDifference', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.catagory')),
            ],
        ),
    ]