# Generated by Django 2.2 on 2019-05-27 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piatrika_form', '0010_auto_20190527_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationtreatment',
            name='farmer_land_village_id',
            field=models.PositiveIntegerField(),
        ),
    ]
