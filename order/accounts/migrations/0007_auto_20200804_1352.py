# Generated by Django 3.0.8 on 2020-08-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200802_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='phone',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
