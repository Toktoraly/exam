# Generated by Django 3.2.4 on 2021-06-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massage',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]