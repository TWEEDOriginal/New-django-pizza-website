# Generated by Django 3.0.6 on 2020-06-07 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200607_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('dressing', models.CharField(max_length=64)),
                ('topping', models.CharField(default='none', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('time_of_order', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
