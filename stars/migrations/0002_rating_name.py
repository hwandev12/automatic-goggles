# Generated by Django 4.1.1 on 2022-09-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]