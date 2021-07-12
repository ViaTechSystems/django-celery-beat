# Generated by Django 3.2.5 on 2021-07-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0013_auto_20200324_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clockedschedule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='crontabschedule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='intervalschedule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='periodictask',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solarschedule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
