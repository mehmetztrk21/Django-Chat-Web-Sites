from django.urls import path
from . import views as v

app_name = 'machine'

urlpatterns = [
    path('', v.ChatListView.as_view(), name='all'),
    path('new/', v.ChatCreateView.as_view(), name='new'),
]
