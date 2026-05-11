from rest_framework import serializers
from .models import Patient, Test, LabReport

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class LabReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabReport
        fields = '__all__'
#तर ModelSerializer ले:

#fields automatically detect गर्छ ✔️
#create/update methods बनाइदिन्छ ✔️
#code छोटो हुन्छ ✔️
#Serializer = Model data → JSON (API format)