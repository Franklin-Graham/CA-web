from django.urls import path
from . import views
urlpatterns = [
    path('',views.fun1,name='fun1'),
    path('detail',views.Detail,name='Detail'),
    path('bot',views.Bot,name='Bot')
]