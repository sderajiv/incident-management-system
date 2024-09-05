from rest_framework.serializers import ModelSerializer
from .models import *

class user_serializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class incident_serializer(ModelSerializer):
    class Meta:
        model = Incident
        # fields = ['reporter_name', 'type_of_incident', 'details']
        fields = '__all__'