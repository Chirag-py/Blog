# Generated by Django 2.2 on 2020-04-07 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200407_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', 'updated', '-timestamp']},
        ),
    ]