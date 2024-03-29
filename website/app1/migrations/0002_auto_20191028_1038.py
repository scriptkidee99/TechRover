# Generated by Django 2.2.6 on 2019-10-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='full_img',
            field=models.CharField(default='/media/imgicon.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_img',
            field=models.ImageField(default='', upload_to='app1/full_images'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='show_img',
            field=models.CharField(default='/media/imgicon.png', max_length=500),
        ),
    ]
