
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from accounts.views import UserProfileListCreateView, userProfileDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    #accounts.profile
    #gets all user profiles and create a new profile
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
]






