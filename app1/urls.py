from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index),
    path('register_user', views.register_user),
    path('login_user', views.login_user),
    path('quotes',views.quotes),
    path('logout/<id>',views.logout),
    path('edit/<id>',views.edit),
    path('update',views.update),
    path('add_quote',views.add_quote),
    path('delete_quote/<id>',views.delete_quote),
    path('user/<id>/<idd>',views.user),
    path('likes/<id>', views.likes)
]