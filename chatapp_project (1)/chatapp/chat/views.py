
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

@login_required
def chat_view(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/chat.html', {'users': users})

@login_required
def get_messages(request, user_id):
    other_user = User.objects.get(id=user_id)
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        recipient__in=[request.user, other_user]
    )
    return render(request, 'chat/messages.html', {'messages': messages, 'other_user': other_user})
