# Generated by Django 4.0.4 on 2022-06-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage_1', '0004_tweets_sentiment_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='sentiment_done',
            field=models.BooleanField(default=False),
        ),
    ]
