# Generated by Django 3.2.8 on 2021-10-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('total_pages', models.PositiveIntegerField()),
                ('url', models.URLField()),
                ('cover_page_url', models.URLField(default='https://github.com/my-personal-repos/library-books/blob/main/cover_photo.jpg?raw=true')),
            ],
        ),
    ]