# Generated by Django 2.2.5 on 2020-01-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200103_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='filename',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
