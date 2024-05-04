from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer

class PatientDetails(APIView):
    def get(self, request, patient_id, dob):
        try:
            patient = Patient.objects.get(patient_id=patient_id, dob=dob)
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({"message": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
