#Imports
import pafy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import filesizeformat
from django.contrib import messages
from .forms import DownloadForm


#When click search button
def download_video(request):
    global context
    form = DownloadForm(request.POST or None)
    if form.is_valid():
        video_url = form.cleaned_data.get("url")
        if 'm.' in video_url:
            video_url = video_url.replace(u'm.', u'')

        elif 'youtu.be' in video_url:
            video_id = video_url.split('/')[-1]
            video_url = 'https://www.youtube.com/watch?v=' + video_id

        try:
            video = pafy.new(video_url)
        except:
            messages.error(request, 'Invalid URL.')
            return render(request, 'home.html',{ 'form': form })

        stream = video.streams
        video_audio_streams = []

        for s in stream:
            video_audio_streams.append({
                'resolution': s.resolution,
                'extension': s.extension,
                'file_size': filesizeformat(s.get_filesize()),
                'video_url': s.url + "&title=" + video.title
            })

        stream_audio = video.audiostreams
        audio_streams = []
        video_streams = []
        
        for s in stream_audio:
            audio_streams.append({
                'resolution': 'Audio',
                'extension': s.extension,
                'file_size': filesizeformat(s.get_filesize()),
                'video_url': s.url + "&title=" + video.title
            })

        context = {
            'form': form,'title': video.title,
            'streams': video_audio_streams,'likes': video.likes,
            'thumb': video.bigthumbhd, 'dislikes' : video.dislikes,
            'duration': video.duration, 'views': video.viewcount,
            'stream_video': video_streams, 'stream_audio': audio_streams
        }

        return render(request, 'home.html', context)

    return render(request, 'home.html',{ 'form': form })


#Handling erors
def error_404(exception, request):
    return redirect('/')


def error_500(request):
    return redirect('/')