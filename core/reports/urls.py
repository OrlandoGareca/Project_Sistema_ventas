from django.urls import path

from core.reports.views import ReportSaleView

urlpatterns = [
    #report
    path('sale/', ReportSaleView.as_view(), name='sale_report'),
]