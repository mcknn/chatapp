from django.urls import path
from django.contrib import admin
from chat.views import chat, add_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat, name='chat'),
    path('add_message/<int:chat_id>', add_message, name='add_message'),
]
