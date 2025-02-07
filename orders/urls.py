from django.urls import path
from .views import UploadOrderExcelAPIView, DownloadOrderExcelAPIView

urlpatterns = [
    path('upload-orders/', UploadOrderExcelAPIView.as_view(), name='upload-orders'),
    path('download-orders/', DownloadOrderExcelAPIView.as_view(), name='download-orders'),
]
