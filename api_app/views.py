import pandas as pd
import io
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse , StreamingHttpResponse
from openpyxl import Workbook
from .models import A
from .serializers import ASerializer

class UploadExcelAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file', None)
        if not file:
            return Response({'error': 'No file uploaded'}, status=400)

        try:
            df = pd.read_excel(file) 
            records = [
                A(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    phone=row['phone'],
                    city=row['city'],
                )
                for index, row in df.iterrows()
            ]
            A.objects.bulk_create(records)  
            return Response({'message': 'Data uploaded successfully'}, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=400)





class DownloadExcelAPIView(APIView):
    def get(self, request, *args, **kwargs):
        records = A.objects.all()
        serializer = ASerializer(records, many=True)

        # ✅ Step 1: Create Excel Workbook
        wb = Workbook()
        ws = wb.active
        ws.append(['first_name', 'last_name', 'email', 'phone', 'city'])  # Header row

        # ✅ Step 2: Add Data to Excel
        for record in serializer.data:
            ws.append([
                record['first_name'],
                record['last_name'],
                record['email'],
                record['phone'],
                record['city']
            ])

        # ✅ Step 3: Save Workbook to Bytes
        excel_stream = io.BytesIO()
        wb.save(excel_stream)
        wb.close()  # 🛠 Fix: Close Workbook to free memory
        excel_stream.seek(0)  # Reset stream pointer

        # ✅ Step 4: Return Excel as File Response
        response = HttpResponse(
            excel_stream.getvalue(),  # 🛠 Fix: Use `.getvalue()`
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

        return response
