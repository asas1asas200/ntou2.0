# Generated by Django 3.0.4 on 2020-03-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobe', '0003_remove_kobepost_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='kobepost',
            name='nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
