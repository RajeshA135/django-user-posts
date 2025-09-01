# from django.urls import path, include
# from .views.signup import SignupAPI
# urlpatterns = [
#  path('signup/',SignupAPI.as_view(),name='signup'),
# ]
from django.urls import path
from .views.signup import SignupAPI
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.user import ProfileView, PostCreateView, PostListView


urlpatterns = [
    # JWT Auth
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # User
    path("register/", SignupAPI.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),

    # Posts
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/create/", PostCreateView.as_view(), name="create_post"),
]
