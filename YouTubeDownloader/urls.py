from django.urls import path
from django.views.generic import RedirectView
from .views import download_video, btn_video


urlpatterns = [
    path('', download_video),
    path('download', btn_video, name='download'),
    path('<string>', RedirectView.as_view(url='/'))    # Exceptions handling
]