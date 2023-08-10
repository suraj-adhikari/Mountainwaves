from django.contrib import admin
from django.urls import path, include
from api.views import UserListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserListCreateView.as_view(), name='user-list-create'),
]