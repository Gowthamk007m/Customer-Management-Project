# Generated by Django 3.0.5 on 2023-01-10 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230110_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]