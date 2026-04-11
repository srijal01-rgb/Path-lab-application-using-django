from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, Test, LabReport
from .serializers import PatientSerializer, TestSerializer, LabReportSerializer
from rest_framework.permissions import IsAuthenticated

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

class LabReportViewSet(viewsets.ModelViewSet):
    queryset = LabReport.objects.all()
    serializer_class = LabReportSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "patients.html", {"patients": patients})

def test_list(request):
    tests = Test.objects.all()
    return render(request, "tests.html", {"tests": tests})

def report_list(request):
    reports = LabReport.objects.select_related("patient").all()
    patients = Patient.objects.all()
    return render(request, "reports.html", {"reports": reports, "patients": patients})
