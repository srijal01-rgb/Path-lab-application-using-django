from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Patient, Test, LabReport
from .serializers import PatientSerializer, TestSerializer, LabReportSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

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
    if request.method == "POST":
        Patient.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            date_of_birth=request.POST.get("date_of_birth"),
        )
        return redirect("patients")  # reload page after saving
    patients = Patient.objects.all()
    return render(request, "patients.html", {"patients": patients})

def test_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")

        if name and price:  # basic validation
            Test.objects.create(
                name=name,
                description=description,
                price=price
            )

        return redirect("tests")

    tests = Test.objects.all()
    return render(request, "tests.html", {"tests": tests})


from .models import LabReport, Patient, Test

def report_list(request):
    if request.method == "POST":
        LabReport.objects.create(
            patient_id=request.POST.get("patient"),
            test_id=request.POST.get("test"),
            result=request.POST.get("result"),
            date_conducted = request.POST.get("date_conducted")
        )
        return redirect("reports")

    reports = LabReport.objects.select_related("patient", "test").all()
    patients = Patient.objects.all()
    tests = Test.objects.all()

    return render(request, "reports.html", {
        "reports": reports,
        "patients": patients,
        "tests": tests
    })
