# Generated by Django 3.1.3 on 2020-11-10 05:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Cashier', '0005_auto_20201110_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethod',
            name='agentbonus',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='resellerbonus',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='standartbonus',
        ),
        migrations.AlterField(
            model_name='enterhistory',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 5, 6, 39, 111525, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exithistory',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 5, 6, 39, 111525, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/uploads/items/default.png', upload_to='uploads/items/ffb85b09-eb53-4154-8188-3c1f03890d1b/'),
        ),
        migrations.AlterField(
            model_name='topuphistory',
            name='record',
            field=models.CharField(default='89743FA0', max_length=8),
        ),
        migrations.AlterField(
            model_name='topuphistory',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 5, 6, 39, 111525, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 5, 6, 39, 111525, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(default='/uploads/foto/default.png', upload_to='uploads/foto/87cf74f4-714a-4334-8898-eb4bb0fdce61/'),
        ),
    ]
