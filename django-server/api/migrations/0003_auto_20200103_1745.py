# Generated by Django 2.2.5 on 2020-01-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200103_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='dataframe',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]