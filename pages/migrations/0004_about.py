# Generated by Django 4.1.5 on 2023-01-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=200)),
                ('description_1', models.TextField(blank=True)),
            ],
        ),
    ]