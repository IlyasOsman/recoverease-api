# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DisasterReport
from .serializers import DisasterReportSerializer


@api_view(["POST"])
def report_disaster(request):
    serializer = DisasterReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_disaster_reports(request):
    reports = DisasterReport.objects.all()
    serializer = DisasterReportSerializer(reports, many=True)
    return Response(serializer.data)
