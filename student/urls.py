from django.urls import path

from . import views


app_name = 'student'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name="create"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('save/', views.save, name="save"),
]
