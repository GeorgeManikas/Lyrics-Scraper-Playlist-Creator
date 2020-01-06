from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'lyrics'
urlpatterns = [
    path('', views.index,name='index'),
    path('song/<int:pk>', views.show_song, name='show_song'),
    path('delete/<int:pk>,', views.delete_song,name='delete_song'),
    path('show_lyrics/', views.show_lyrics, name='show_lyrics'),
    path('show_playlist',login_required(views.ShowPlayList.as_view()),name='show_playlist'),
    path('save_playlist', views.save_playlist,name='save_playlist'),
    path('to_pdf/<int:pk>', views.write_pdf_view, name='write_to_pdf'),
    path('playlist_to_pdf/', views.playlist_to_pdf, name='playlist_to_pdf'),
    
]

