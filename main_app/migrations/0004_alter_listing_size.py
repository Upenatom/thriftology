# Generated by Django 4.1.1 on 2022-09-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large')], default='S', max_length=3),
        ),
    ]
