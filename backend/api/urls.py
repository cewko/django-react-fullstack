from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path("user/register/", views.CreateUserView.as_view(), name="user-register"),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("token/refresh", TokenRefreshView.as_view(), name="token-refresh"),
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
]