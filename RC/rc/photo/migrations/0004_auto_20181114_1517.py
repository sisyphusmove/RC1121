# Generated by Django 2.1.2 on 2018-11-14 06:17

from django.db import migrations, models
import django.db.models.deletion
import photo.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20181114_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photo.Album'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=photo.fields.ThumbnailImageField(blank=True, upload_to='photo/%Y/%m'),
        ),
    ]
