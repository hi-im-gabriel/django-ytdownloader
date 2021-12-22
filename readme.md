 <h1 align="center">YouTube Downloader</h1>
   <p align="center">
    <a href="https://github.com/gabzin/django-ytdownloader/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-red.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Django-green.svg" />
    </a>
	<p align="center">⭐️ Star this project ⭐️</p>
  </p>
<a href="https://downtube.vercel.app/"><p align="center">https://downtube.vercel.app/</p></a>
<p align="center">
  <a href="https://downtube.vercel.app/"><img src="https://iili.io/YfwYva.png"></a>
</p>

# Updates
> # v2021.12
> 
> #### Added:
> 
> - YouTube API to get likes/favs count
> - Visual enhancement
> - Particles JS
> - Bootstrap icons
>
> #### Bug fixes:
>
> - Opening video/audio links instead of downloading
>
> # v2021.11
> 
> #### Added:
> 
> - Migration from pafy/youtube-dl to pytube (Performance reasons)
> - Visual enhancement
>
> #### Bug fixes:
>
> - Error 404 handling
>
> #### Future updates:
>
> - 1080p60+ downloads
> - Dark/Light mode option


# Requirements
  - Python3
  - Pip3
  - Git
  - YouTube V3 API KEY (otherwise, likes count aren't avalible with pytube anymore):
  
  <a href="https://developers.google.com/youtube/v3">https://developers.google.com/youtube/v3</a>
  
 <p align="center">
    <img src="https://iili.io/YfwpF1.png" width="80%">
</p>
  

# Installation

```bash
git clone https://github.com/gabzin/django-ytdownloader
cd django-ytdownloader
pip3 install -r requirements.txt
```

# Starting server

```bash
python manage.py runserver
```