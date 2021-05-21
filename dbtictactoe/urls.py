from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('game',views.game,name='game'),
    path('submit',views.submit,name='submit'),
    path('view',views.view,name='view')
]