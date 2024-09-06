from rest_framework import serializers
from .models import Leads

class LeadCreateSerializer(serializers.ModelSerializer):
    barkId=serializers.CharField()
    
    def validate(self, data):
        
        if data['barkId'] == None:
            raise serializers.ValidationError("Bark Id cannot be left empty.")
        
        return super().validate(data)
        
    class Meta:
        model=Leads
        fields=['barkId']
        

class LeadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'


class LeadFetchSerializer(serializers.ModelSerializer):
    barkId=serializers.CharField()
    
    def validate(self, data):
        
        if data['barkId'] == None:
            raise serializers.ValidationError("Bark Id cannot be left empty.")
        
        return super().validate(data)
        
    class Meta:
        model=Leads
        fields=['barkId']