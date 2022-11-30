# Generated by Django 4.1.3 on 2022-11-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=50)),
                ('icon_uri', models.CharField(max_length=50)),
                ('manifest_uri', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
            ],
        ),
    ]