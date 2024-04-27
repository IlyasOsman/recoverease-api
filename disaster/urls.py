# urls.py
from django.urls import path
from .views import report_disaster, get_disaster_reports

urlpatterns = [
    path("report/", report_disaster, name="report_disaster"),
    path("reports/", get_disaster_reports, name="get_disaster_reports"),
]
