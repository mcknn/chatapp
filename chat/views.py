from django.shortcuts import render
from .models import *


def chat(request):
    chat_obj = Chat(user=request.user)
    chat_obj.save()

    messages = Message.objects.filter(chat=chat_obj)
    content = [dict(content=m.content, sender=m.sender) for m in messages]
    return render(request, 'app.html', {'messages': content, 'chat_id': chat_obj.pk})


def add_message(request, chat_id):
    chat_obj = Chat.objects.get(pk=chat_id)

    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content:
            Message.objects.create(content=content, chat=chat_obj)

    messages = Message.objects.filter(chat=chat_obj)
    content = [dict(content=m.content, sender=m.sender) for m in messages]
    return render(request, 'chat.html', {'messages': content})


