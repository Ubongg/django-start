# Generated by Django 3.1.7 on 2021-03-16 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thimb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thimb',
            new_name='thumb',
        ),
    ]
