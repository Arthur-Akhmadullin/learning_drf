# Generated by Django 3.2.15 on 2022-09-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField(blank=True)),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
