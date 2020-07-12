from django.urls import path
from . import views

urlpatterns = [
    path('',views.notes_list, name='notes_list'),
    path('note/<int:pk>/',views.note_detail, name='note_detail'),
    path('note/new/',views.note_new, name='note_new'),
    path('note/edit/<int:pk>/',views.note_edit, name='note_edit'),
    path('note/remove/<int:pk>',views.note_remove, name='note_remove'),
    path('signup/', views.signup, name='signup')
]