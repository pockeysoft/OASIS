from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("explore/", view=views.ExploreUsers.as_view(), name="explore"),
    path("<int:user_id>/follow/", view=views.FollowUser.as_view(), name="follow_user"),
    path("<int:user_id>/unfollow/", view=views.UnfollowUser.as_view(), name="unfollow_user"),
    path("search/", view=views.Search.as_view(), name="search"),
    path("<str:username>/images", view=views.UserAllImages.as_view(), name="user_all_images"),
    path("<str:username>/following", view=views.UserFollowing.as_view(), name="user_following"),
    path("<str:username>/followers", view=views.UserFollowers.as_view(), name="user_followers"),
    path("<str:username>/password", view=views.ChangePassword.as_view(), name="change_password"),
    path("<str:username>/", view=views.UserProfile.as_view(), name="user_profile"),
    path("login/facebook/", view=views.FacebookLogin.as_view(), name='fb_login'),
]
