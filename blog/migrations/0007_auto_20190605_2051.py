# Generated by Django 2.2.1 on 2019-06-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
