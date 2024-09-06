from django.shortcuts import render
from .models import Leads
from rest_framework import generics
from rest_framework.views import APIView
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Leads

# Create your views here.
class LeadsCreateView(APIView):
    serializer_class = serializers.LeadCreateSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            item, created = Leads.objects.get_or_create(barkId=serializer.validated_data.get('barkId'))
            return Response(data={"success":True,"message":"Lead Created Successfully","data":{"barkId": item.barkId}}, status=status.HTTP_201_CREATED)

        return Response(data={"success":False,"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        


class LeadsListView(APIView):
    serializer_class = serializers.LeadListSerializer
    # permission_classes = []

    def get(self, request):
        leads = Leads.objects.all().values_list()
        return Response(data={"success":True,"message":"Leads Retrieved Successfully","data":{"leads": leads}}, status=status.HTTP_200_OK)



class LeadsFetchView(APIView):
    serializer_class = serializers.LeadFetchSerializer
    # permission_classes = []

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            leads = Leads.objects.filter(barkId=serializer.validated_data.get("barkId"))
            if(leads.exists()):
                return Response(data={"success":True,"message":"Lead Fetched Successfully","data":{"lead": leads.values().first()}}, status=status.HTTP_200_OK)
            
            
            return Response(data={"success":False,"error":"No Such Lead Exists"}, status=status.HTTP_404_NOT_FOUND)
           

        
        return Response(data={"success":False,"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)