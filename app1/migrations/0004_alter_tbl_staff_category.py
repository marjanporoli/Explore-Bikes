# Generated by Django 4.0.1 on 2022-01-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app1', '0003_tbl_staff_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_staff',
            name='category',
            field=models.CharField(default='Nil', max_length=15),
        ),
    ]
