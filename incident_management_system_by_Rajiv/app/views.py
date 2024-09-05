from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Incident
from .serializers import user_serializer, incident_serializer
from django.utils.crypto import get_random_string
import datetime, requests
# from pgeocode import Nominatim
import pgeocode

@api_view(['GET'])
def test(request):
    return Response('Ok')


def get_location_by_pincode(country_code,pincode):
    # country_code = request.query_params.get('country_code')
    # pincode = request.query_params.get('pincode')
    url = f"http://api.zippopotam.us/{country_code}/{pincode}" 
    response = requests.get(url)
    # print(response)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        city = data['places'][0]['place name']
        state = data['places'][0]['state']
        country = data['country']
        if city and country:
            return city, state, country
            # return Response({'city': city, 'state': state, 'country': country})
    else:
        return None
        # return Response({'error': 'Invalid pincode'})

@api_view(['POST'])
def register_user(request):
    country_code = request.query_params.get('country_code')
    pincode = request.query_params.get('pincode')
    loc = get_location_by_pincode(country_code, pincode)
    print(loc[2])
    data = {
    'name' : request.data.get('name'),
    'email' : request.data.get('email'),
    'mobile' : request.data.get('mobile'),
    'add' : request.data.get('address'),
    'pin' : request.data.get('pin_code'),
    'city' : loc[0],
    'state' : loc[1],
    'country' : loc[2]
    }
    serializer = user_serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = user_serializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_incident(request):
    data = {
        'incident_id' : f"RMG{get_random_string(5)}{datetime.datetime.now().year}",
        'type_of_incident': request.data.get('type'),
        'reporter_name' : request.data.get('reporter_name'),
        'details' : request.data.get('details'),
        'priority' : request.data.get('priority'),
        'status': request.data.get('status')
   }
    serializer = incident_serializer(data=data)  
    if serializer.is_valid(): 
        serializer.save()  
        return Response(serializer.data)  
    return Response(serializer.errors)  

@api_view(['GET'])  
def get_incidents(request):  
   incidents = Incident.objects.all()  
   serializer = incident_serializer(incidents, many=True)  
   return Response(serializer.data) 


@api_view(['GET'])
def get_incident_detail(request, incident_id):
    print(incident_id)
    try:
        incident = Incident.objects.get(incident_id=incident_id)
        res = incident_serializer(incident).data
        print(res)
        return Response(res)
    except:
        return Response({'err': 'Invalid Incident_id'})

@api_view(['PUT'])
def update_incident(request, incident_id):
    req = {
        'type_of_incident': request.data.get('type'),
        'reporter_name' : request.data.get('reporter_name'),
        'details' : request.data.get('details'),
        'priority' : request.data.get('priority'),
        'status' : request.data.get('status')
    }
    try:
        incident = Incident.objects.get(incident_id=incident_id)
        serializer = incident_serializer(incident, data=req, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    except Exception as e:
        return Response({"err": "invalid incidentId"})
    
@api_view(['GET'])
def search_incident(request):
    incident_id = request.data.get('incident_id')
    print(incident_id)
    # if incident_id:
    try:
        incident = Incident.objects.get(incident_id=incident_id)
        res = incident_serializer(incident).data
        print(res)
        return Response(res)
    except:
        return Response({'msg': 'Incident not available'})
    # else:
    #     return Response({'msg': 'check and type correct incident_id'})

@api_view(['GET'])
def get_loc_(request):
    data = pgeocode.Nominatim('IN')
    loc=data.query_postal_code("843108")
    # print(data)
    return Response(loc)


    