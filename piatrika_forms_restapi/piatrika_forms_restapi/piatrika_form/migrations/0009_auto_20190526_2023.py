# Generated by Django 2.2.1 on 2019-05-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piatrika_form', '0008_auto_20190526_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='Farmers_id',
            field=models.PositiveIntegerField(),
        ),
    ]
