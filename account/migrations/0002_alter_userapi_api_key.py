# Generated by Django 4.2 on 2023-04-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapi',
            name='api_key',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
