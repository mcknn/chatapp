from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    content = models.TextField()
    from_user = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    @property
    def sender(self):
        return self.chat.user.username if self.from_user else 'Bot'
