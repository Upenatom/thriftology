# Generated by Django 4.1.1 on 2022-09-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='condition',
            field=models.CharField(choices=[('N', 'New'), ('L', 'Like New'), ('G', 'Good'), ('F', 'Fair')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=15),
        ),
    ]