# Generated by Django 3.2.5 on 2021-07-08 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Janrlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kitoblar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('muallif', models.CharField(max_length=50)),
                ('fayl', models.FileField(upload_to='media/doc/%Y/%m/%d/')),
                ('nashr_yili', models.IntegerField(null=True)),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='')),
                ('audio', models.FileField(blank=True, null=True, upload_to='media/audio/%Y/%m/%d/')),
                ('sahifalar', models.IntegerField(null=True)),
                ('janri', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.janrlar')),
            ],
        ),
    ]
