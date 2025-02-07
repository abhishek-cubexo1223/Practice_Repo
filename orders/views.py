import pandas as pd
import io
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Order
from .serializers import OrderSerializer

# ✅ **Upload Order Data from Excel**
class UploadOrderExcelAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file', None)
        if not file:
            return Response({'error': 'No file uploaded'}, status=400)

        try:
            df = pd.read_excel(file)  
            records = [
                Order(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    phone=row['phone'],
                    city=row['city'],
                    total_amount=row['total_amount'],
                    status=row['status'],
                )
                for index, row in df.iterrows()
            ]
            Order.objects.bulk_create(records)  
            return Response({'message': 'Orders uploaded successfully'}, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


# ✅ **Download Order Data as Excel**
class DownloadOrderExcelAPIView(APIView):
    def get(self, request, *args, **kwargs):
        records = Order.objects.all()
        serializer = OrderSerializer(records, many=True)

        # ✅ Create Excel Workbook
        wb = Workbook()
        ws = wb.active
        ws.append(['first_name', 'last_name', 'email', 'phone', 'city', 'total_amount', 'status'])  # Header

        # ✅ Add Data to Excel
        for record in serializer.data:
            ws.append([
                record['first_name'],
                record['last_name'],
                record['email'],
                record['phone'],
                record['city'],
                record['total_amount'],
                record['status']
            ])

        # ✅ Save Workbook to Bytes
        # import pdb;pdb.set_trace()
        excel_stream = io.BytesIO()
        wb.save(excel_stream)
        wb.close()  
        excel_stream.seek(0)  

        # ✅ Return Excel as File Response
        response = HttpResponse(
            excel_stream.getvalue(),  
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = 'attachment; filename="orders.xlsx"'

        return response
