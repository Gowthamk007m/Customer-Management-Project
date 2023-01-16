from . import views

from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin_home',views.home,name='home'),
    path('',views.products,name='products'),
    path('customer/<str:pk>/',views.user_data,name='customer'),
    path('user/',views.user_page,name='userpage'),
    path('create_order/<str:pk>/',views.create_order,name='create_order'),
    path('Update_order/<str:pk>',views.Update_Order,name='update_order'),
    path('Delete_order/<str:pk>',views.Delete_Order,name='delete_order'),
    path('login/',views.Login_page,name='login'),
    path('register/',views.Register,name='register'),
    path('logout/',views.LogoutUser,name='logout'),
    path('accounts/',views.user_acc,name='accounts'),


    path('reset_password/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),


]
