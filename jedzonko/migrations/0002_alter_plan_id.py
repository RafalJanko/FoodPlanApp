# Generated by Django 4.0.2 on 2022-02-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
