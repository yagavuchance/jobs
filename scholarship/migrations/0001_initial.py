# Generated by Django 5.0.6 on 2024-06-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('title', models.CharField(max_length=200)),
                ('deadline', models.DateField()),
                ('link', models.URLField()),
            ],
        ),
    ]
