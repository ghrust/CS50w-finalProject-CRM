# Generated by Django 3.1.5 on 2021-01-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20210124_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='company',
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ManyToManyField(related_name='companies', to='crm.Company', verbose_name='company of which the client is a customer'),
        ),
    ]
