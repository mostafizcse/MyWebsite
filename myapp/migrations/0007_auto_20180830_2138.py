# Generated by Django 2.0.7 on 2018-08-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_teammember_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
