# Generated by Django 3.2.3 on 2021-05-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]