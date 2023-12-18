from django.urls import path

from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('cbview/', views.Tasklist.as_view(), name='cbview'),
    path('cbdetail/<int:pk>', views.Detail.as_view(), name='cbdetail'),
    path('cbupdate/<int:pk>', views.Update.as_view(), name='cbupdate'),
    path('cbdelete/<int:pk>', views.Delete.as_view(), name='cbdelete')

]
