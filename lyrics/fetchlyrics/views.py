from requests import Request, Session
from requests_html import HTMLSession
from allauth.account.decorators import login_required
from django.http import HttpResponse
from .utils import render_to_pdf

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import SearchForm
from .models import Playlist



BASE_URL = 'https://api.lyrics.ovh/v1/'

def index(request):
    request.session['lyrics'] = ''
    request.session['title'] = ''
    request.session['artist'] = ''
    form = SearchForm()
    context = {'form':form}
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            request.session['title'] = title.title()
            artist = form.cleaned_data['artist']
            request.session['artist'] = artist.title()
            DEST_URL = f'{BASE_URL}{artist}/{title}'
            session = HTMLSession()
            req = session.get(DEST_URL).json()
            if 'error' in req.keys():
                request.session['title'] = ''
                request.session['artist'] = ''
                request.session['lyrics'] = 'No lyrics found'
                return redirect('lyrics:show_lyrics')
            else:
                request.session['lyrics'] = req['lyrics']
                return redirect('lyrics:show_lyrics')    
    return render(request, 'fetchlyrics/index.html', context)

def show_lyrics(request):
    return render(request, 'fetchlyrics/show_lyrics.html')

class ShowPlayList(ListView):
    
    model = Playlist
    template_name = 'fetchlyrics/playlist.html'
    context_object_name = 'songs'
     
    def get_queryset(self):
        qs = self.model.objects.filter(user__id=self.request.user.id)
        return qs

from django.contrib import messages    
@login_required()
def save_playlist(request):
    
    artist = str(request.session.get('artist'))
    title = str(request.session.get('title'))
    lyrics = str(request.session.get('lyrics'))
    new_item = Playlist()
    new_item.title = title
    new_item.artist = artist
    new_item.lyrics = lyrics
    new_item.user = request.user
    new_item.save()
    messages.success(request,'Song added to playlist')
    return redirect('lyrics:index')

def show_song(request, pk):
    song = Playlist.objects.get(pk=pk)  
    return render(request, 'fetchlyrics/lyrics.html', {'song':song})

def delete_song(request,pk):
    song = Playlist.objects.get(pk=pk)
    if request.method == "POST":
        song.delete()
        return redirect('lyrics:show_playlist')
    return render(request,'fetchlyrics/delete.html',{'song':song})


def write_pdf_view(request,pk):
    song = Playlist.objects.get(pk=pk)
    data = {
        'title' : song.title,
        'artist' : song.artist,
        'lyrics' : song.lyrics,
    }
    pdf = render_to_pdf('fetchlyrics/pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

    
def playlist_to_pdf(request):
    songs = Playlist.objects.all()
    context = {
        'songs': songs
    }

    pdf = render_to_pdf('fetchlyrics/pdf_list.html',context)
    return HttpResponse(pdf, content_type='application/pdf')
    

        

    
   
    
    
    