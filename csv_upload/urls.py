from django.urls import path
from .views import upload_csv, download_csv

urlpatterns = [
    path('upload-csv/', upload_csv, name='upload_csv'),
    path('download-csv/', download_csv, name='download_csv'),

    
]