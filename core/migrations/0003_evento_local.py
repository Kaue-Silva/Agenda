# Generated by Django 3.2.8 on 2021-10-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211029_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
