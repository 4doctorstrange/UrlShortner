# Generated by Django 3.1.6 on 2021-02-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210216_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='short_urls',
            name='short_url',
            field=models.CharField(max_length=200),
        ),
    ]