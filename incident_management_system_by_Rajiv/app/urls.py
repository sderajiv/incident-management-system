from django.urls import path
from .views import *

urlpatterns=[
    path('', test, name='test'),
    path('create-user/', register_user, name='register_user'),
    path('get-all-user/', get_users, name='get_all_users'),
    path('create-incident/', create_incident, name='create_incident'),
    path('get-incidents/', get_incidents, name='get_all_incidents_list'),
    path('get-incident/<incident_id>/', get_incident_detail, name='get_incident_detail'),
    path('update-incident/<incident_id>/', update_incident, name='update_incident'),
    path('search-incident/', search_incident, name='search_incident'),
    # path('get-loc/<str:country_code>/<pincode>/',get_location_by_pincode, name='get_loc')

]