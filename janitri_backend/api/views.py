from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Patient, HeartRate
from .serializers import UserSerializer, PatientSerializer, HeartRateSerializer

# User Registration
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login
@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email, password=password).first()
        if user:
            return Response({"message": "Login successful", "user": UserSerializer(user).data})
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# Add Patient
@api_view(['POST'])
def add_patient(request):
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get Patients of a User
@api_view(['GET'])
def get_patients(request, user_id):
    if request.method == 'GET':
        patients = Patient.objects.filter(user_id=user_id)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

# Record Heart Rate
@api_view(['POST'])
def record_heart_rate(request):
    if request.method == 'POST':
        serializer = HeartRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get Heart Rates of a Patient
@api_view(['GET'])
def get_heart_rates(request, patient_id):
    if request.method == 'GET':
        heart_rates = HeartRate.objects.filter(patient_id=patient_id)
        serializer = HeartRateSerializer(heart_rates, many=True)
        return Response(serializer.data)

