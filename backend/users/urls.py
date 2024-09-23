from django.urls import path
from .views import CreateUserView, LoginView, GetUsersView, LogOutView, DeleteUserView, EditUserView

urlpatterns = [
    path('', GetUsersView.as_view(), name='get_users'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('delete/<int:user_id>/', DeleteUserView.as_view(), name='delete_user'),
    path('edit/<int:user_id>/', EditUserView.as_view(), name='edit_user'),
    path('login/', LoginView.as_view(), name='login_user'),
    path('logout/', LogOutView.as_view(), name='logout_user'),
]
