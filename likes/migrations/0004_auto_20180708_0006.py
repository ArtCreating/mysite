# Generated by Django 2.0.6 on 2018-07-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0003_auto_20180707_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likecount',
            name='liked_num',
            field=models.IntegerField(default=1),
        ),
    ]
