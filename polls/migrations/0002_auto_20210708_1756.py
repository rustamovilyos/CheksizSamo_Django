# Generated by Django 3.2.5 on 2021-07-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitoblar',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='media/audio/'),
        ),
        migrations.AlterField(
            model_name='kitoblar',
            name='fayl',
            field=models.FileField(upload_to='media/doc/'),
        ),
    ]
