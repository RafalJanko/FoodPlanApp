# Generated by Django 4.0.2 on 2022-02-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0002_alter_plan_options_alter_plan_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='preparing',
            field=models.CharField(default='', max_length=500),
        ),
    ]