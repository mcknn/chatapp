# Generated by Django 5.0.2 on 2024-02-09 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_message_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='from_user',
            field=models.BooleanField(default=True),
        ),
    ]
