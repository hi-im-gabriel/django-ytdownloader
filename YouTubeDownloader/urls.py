from django.conf.urls import handler404, handler500
from django.urls import path
from .views import download_video

handler404 = 'YouTubeDownloader.views.error_404'
handler500 = 'YouTubeDownloader.views.error_500'

urlpatterns = [
    path('', download_video)
]

