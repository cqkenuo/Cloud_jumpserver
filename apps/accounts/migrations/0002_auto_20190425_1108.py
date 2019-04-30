# Generated by Django 2.1.7 on 2019-04-25 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudaccount',
            name='cloud_provider',
            field=models.CharField(choices=[('Aliyun', 'Aliyun'), ('Qcloud', 'Qcloud')], default='', max_length=50, verbose_name='Cloud Provider'),
        ),
    ]
