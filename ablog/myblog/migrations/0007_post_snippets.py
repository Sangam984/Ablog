# Generated by Django 4.2.5 on 2023-09-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippets',
            field=models.CharField(default='Click Here', max_length=200),
        ),
    ]