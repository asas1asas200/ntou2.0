# Generated by Django 3.0.4 on 2020-03-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobe', '0012_kobepost_posttime'),
    ]

    operations = [
        migrations.AddField(
            model_name='kobepost',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]