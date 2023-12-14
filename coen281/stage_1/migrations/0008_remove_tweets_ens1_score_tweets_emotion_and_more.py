# Generated by Django 4.0.4 on 2022-06-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage_1', '0007_tweets_ens1_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweets',
            name='ens1_score',
        ),
        migrations.AddField(
            model_name='tweets',
            name='emotion',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='tweets',
            name='sentiment_score',
            field=models.IntegerField(default=0),
        ),
    ]
