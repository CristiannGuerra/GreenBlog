# Generated by Django 3.2.9 on 2021-12-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20211217_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default='defatult tag', max_length=255),
        ),
    ]
