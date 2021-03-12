from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .forms import ChatForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import backend
from django.utils import timezone

# Create your views here.


class ChatCreateView(LoginRequiredMixin, CreateView):
    login_url = 'accounts:login'
    form_class = ChatForm
    model = backend

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ChatListView(LoginRequiredMixin, ListView):
    model = backend

    def get_queryset(self):
        return backend.objects.filter(posted_at__lte=timezone.now()).order_by('posted_at')
