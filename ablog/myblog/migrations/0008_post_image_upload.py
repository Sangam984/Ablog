# Generated by Django 4.0.2 on 2023-09-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_post_snippets'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_upload',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]