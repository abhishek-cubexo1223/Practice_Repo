from django.urls import path
from .views import UploadExcelAPIView , DownloadExcelAPIView

urlpatterns = [
    path("upload_excel_for_A_model/",UploadExcelAPIView.as_view() , name="upload-excel-for-a-model"),
    path("download_file/",DownloadExcelAPIView.as_view(), name="download_File")
]

