# Generated by Django 3.0.7 on 2020-07-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20200725_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(default='media/none/nothumb.jpg', upload_to='media'),
        ),
    ]
