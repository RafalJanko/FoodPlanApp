# Generated by Django 2.2.6 on 2022-02-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ['name', '-created']},
        ),
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]