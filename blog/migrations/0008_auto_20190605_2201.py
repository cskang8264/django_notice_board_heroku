# Generated by Django 2.2.1 on 2019-06-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190605_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imageText',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='blog',
            name='imageTitle',
            field=models.CharField(default='', max_length=50),
        ),
    ]
