# Generated by Django 2.0.7 on 2018-09-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20180902_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuretitle',
            name='details',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]