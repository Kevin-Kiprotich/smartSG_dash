from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import OffenceSerializer
from .models import Owner,Rider,Offence,Location

class LoginView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')

        try:
            user=Owner.objects.get(email=email)
            if user.check_password(password):
                return Response({'Success':True,'Message':'Login Successful'})
        except Owner.DoesNotExist:
            return Response ({'Success':False, 'Message':False})

class Register(APIView):
    def post(self,request):
        first_name=request.data.get('first_name')
        last_name=request.data.get('last_name')
        Owner_ID=request.data.get('owner_ID')
        email=request.data.get('email')
        phone_number=request.data.get('phone_number')
        password=request.data.get('password')

        try:
            user=Owner.objects.get(email=email)
            return Response({'Success':False,'Message':'The email is already taken'})
        except Owner.DoesNotExist:
            user=Owner.objects.create_user(email=email,first_name=first_name,last_name=last_name,Owner_ID=Owner_ID,
                                           phone_number=phone_number,password=password)
            user.save()
            return Response({'Success':True,'Message':"Registration Successfull"})
        
class AssignDriver(APIView):
    def post(self,request):
        first_name=request.data.get('first_name')
        last_name=request.data.get('last_name')
        ID_Number=request.data.get('ID_Number')
        brand=request.data.get('brand')
        model=request.data.get('model')
        number_plate=request.data.get('number_plate')

        try:
            rider=Rider.objects.get('number_plate')
            return Response({'Success':False,'Message':'Vehicle Already Assigned'})
        except Rider.DoesNotExist:
            rider=Rider(first_name=first_name,last_name=last_name,ID_Number=ID_Number,brand=brand,model=model,number_plate=number_plate)
            rider.save()
            return Response({"Success":True,"Message":"Registration Successful"})

class ReportOffence(APIView):
    def post(self,request):
        number_plate=request.data.get('number_plate')
        latitude=float(request.data.get('latitude'))
        longitude=float(request.data.get('longitude'))
        speed=float(request.data.get('speed'))
        speedLimit=float(request.data.get('speed_limit'))
        try:
            rider=Rider.objects.get(number_plate=number_plate)
            rider.offence_count+=1
            rider.save()
            offence=Offence(latitude=latitude,longitude=longitude,speed=speed,speed_limit=speedLimit,vehicle=rider)
            offence.save()
            return Response({"Success":True,"Message":"Offence Reported"})
        except Rider.DoesNotExist:
            return Response({'Success':False,"Message":"Unrecognized Number Plate"})

class StoreLocation(APIView):
    def post(self,request):
        number_plate=request.data.get('number_plate')
        latitude=float(request.data.get('latitude'))
        longitude=float(request.data.get('longitude'))
        speed=float(request.data.get('speed'))
        rider=Rider.objects.get(number_plate=number_plate)
        location=Location(latitude=latitude,longitude=longitude,speed=speed,vehicle=rider)
        location.save()

        return Response({'Success':True,"Message":"Location Stored Successfully"})

def ShowOffences(request):
    template=loader.get_template('dash.html')
    return HttpResponse(template.render())

class OffenceList(APIView):
    def get(self, request):
        offences = Offence.objects.all()
        serializer = OffenceSerializer(offences, many=True)
        return Response(serializer.data)

    def post(self, request):
        number_plate=request.data.get('number_plate')
        serializer = OffenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LocationsList(APIView):
    def get(self, request):
        offences = Offence.objects.all()
        serializer = OffenceSerializer(offences, many=True)
        return Response(serializer.data)