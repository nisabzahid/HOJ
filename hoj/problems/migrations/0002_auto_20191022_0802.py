# Generated by Django 2.2.6 on 2019-10-22 08:02

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='sample_input',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='sample_output',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=0),
            preserve_default=False,
        ),
    ]
