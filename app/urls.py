from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.base,name='base'),
    path('contact/',views.contact,name='contact'),
    path('form/',views.form,name='form'),
    path('savedata/',views.savedata,name='savedata'),
    path('savename/',views.savename,name='savename'),
    path('delname/',views.delname,name='delname'),
    path('get_home/',views.get_home,name="get_home"),
    path('todo_post/',views.todo_post,name="todo_post"),
    path('get_todo/',views.get_todo, name ='get_todo'),
    path('update/',views.update, name ='update'),
    path('saveform/',views.saveform, name ='saveform'),
    path('delformconatct/', views.delformconatct, name="delformconatct"),
    path('Updateconatct/', views.Updateconatct, name="Updateconatct"),
    path('upform/', views.upform, name="upform"),
]
