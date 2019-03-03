from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .models import User_details,User_location_details,Driver_details,Driver_location_details,Booking,Hospital_details

from .serializers import User_details_Serializer,User_location_details_Serializer,Driver_details_Serializer,Driver_location_details_Serializer,Booking_Serializer,Hospital_details_Serializer

from rest_framework.permissions import  AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .mixins import SerializeMixin,SerializeMixin1
import json


class User_details_CR(ListCreateAPIView):
    queryset=User_details.objects.all()
    serializer_class=User_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset   = self.get_queryset()
        serializer = User_details_Serializer(queryset, many=True)
        return Response({'status':True,'code':1001,'message':'Author Details','data':serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'data':[{'U_ID':serializer.data.get('U_ID')}],'status':True,'code':1001,'message':'Author Details'}, status=status.HTTP_201_CREATED, headers=headers)


class User_details_UD(RetrieveUpdateDestroyAPIView):
    queryset=User_details.objects.all()
    serializer_class=User_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object() # here the object is retrieved
        serializer = self.get_serializer(instance)
        return Response({'data':serializer.data,'status':True,'code':1001,'message':'Author Details'})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'data':serializer.data,'status':True,'code':1001,'message':'Author Details'})
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



# class User_login_details_CR(ListCreateAPIView):
#     queryset=User_login_details.objects.all()
#     serializer_class=User_login_details_Serializer
#     # authentication_classes=[JSONWebTokenAuthentication,]
#     # permission_classes=[IsAuthenticated,]
#
# class User_login_details_UD(RetrieveUpdateDestroyAPIView):
#     queryset=User_login_details.objects.all()
#     serializer_class=User_login_details_Serializer
#     # authentication_classes=[JSONWebTokenAuthentication,]
#     # permission_classes=[IsAuthenticated,]


class User_location_details_CR(ListCreateAPIView):
    queryset=User_location_details.objects.all()
    serializer_class=User_location_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset   = self.get_queryset()
        serializer = User_location_details_Serializer(queryset, many=True)
        return Response({'data':serializer.data,'status':True,'code':1001,'message':'Author Details'})


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'status':True,'code':1001,'message':'User_details_CR'})



class User_location_details_UD(RetrieveUpdateDestroyAPIView):
    queryset=User_location_details.objects.all()
    serializer_class=User_location_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object() # here the object is retrieved
        serializer = self.get_serializer(instance)
        return Response({'data':serializer.data,'status':True,'code':1001,'message':'Author Details'})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'data':serializer.data,'status':True,'code':1001,'message':'Author Details'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



class Driver_details_CR(ListCreateAPIView,SerializeMixin,SerializeMixin1):
    queryset=Driver_details.objects.all()
    serializer_class=Driver_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset   = self.get_queryset()
        queryset   = queryset.filter(availability=True)
        # mylist=[]
        # for item in queryset:
        #          mylist.append({'D_ID':item.get("D_ID")})
        serializer = Driver_details_Serializer(queryset, many=True)
        return Response({'data':serializer.data,'status':True,'code':1001,'message':'Driver Details'})

    def create(self, request, *args, **kwargs):
        QS=Driver_details.objects.all()
        resp=self.myserialize(QS)

        username=self.request.data.get('username',None)
        print(username)
        resp1=self.myserialize1(QS,username)
        print(resp)
        print(type(resp))

        print(resp1)
        print(type(resp1))


        li = list(username.split(","))
        print(li)
        print(type(li))
        if  li[0] in resp:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'data':[{'D_ID':resp1}],'status':True,'code':1001,'message':'Author Details'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'data':"",'status':False,'code':100,'message':'Driver Not Exist'})


class Driver_details_UD(RetrieveUpdateDestroyAPIView):
    queryset=Driver_details.objects.all()
    serializer_class=Driver_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object() # here the object is retrieved
        serializer = self.get_serializer(instance)
        return Response({'data':serializer.data,'status':True,'code':1001,'message':'Driver Details'})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'data':serializer.data,'status':True,'code':1001,'message':'Driver Details'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



class Driver_location_details_CR(ListCreateAPIView):
    queryset=Driver_location_details.objects.all()
    serializer_class=Driver_location_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]

class Driver_location_details_UD(RetrieveUpdateDestroyAPIView):
    queryset=Driver_location_details.objects.all()
    serializer_class=Driver_location_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]


class Booking_CR(ListCreateAPIView):
    queryset=Booking.objects.all()
    serializer_class=Booking_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]

class Booking_UD(RetrieveUpdateDestroyAPIView):
    queryset=Booking.objects.all()
    serializer_class=Booking_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]


class Hospital_details_CR(ListCreateAPIView):
    queryset=Hospital_details.objects.all()
    serializer_class=Hospital_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
            #print("Should be:", 278.546, "km")


    #
    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset   = self.get_queryset()
    #     #queryset   = queryset.filter(type=)
    #     serializer = Hospital_details_Serializer(queryset, many=True)
    #     return Response({'data':serializer.data,'status':True,'code':1001,'message':'Author Details'})
    #
    #
    # def create(self, request, *args, **kwargs):
    #     # ty=self.request.data.get('type')
    #     # print(ty)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     #self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response({'status':True,'code':1001,'message':'User_details_CR'})
    #

import math
class DistanceListAPIView(APIView):
    queryset=Hospital_details.objects.all()
    serializer_class=Hospital_details_Serializer
    def get(self,request,format=None):
            lat_list=[]
            long_list=[]
            qs=Hospital_details.objects.all()
            lat1=self.request.GET.get('lat')
            lat1=float(lat1)
            #print(lat1)
            lon1=self.request.GET.get('long')
            lon1=float(lon1)
            #print(lon1)
            typ=self.request.GET.get('type')
            list=[]
            lat_list=[obj.h_latitude for obj in Hospital_details.objects.filter(type=typ)]
            lat_list.sort()
            #print(lat_list)
            long_list=[obj.h_longitude for obj in Hospital_details.objects.filter(type=typ)]
            long_list.sort()
            #print(long_list)
            id_list=[obj.H_ID for obj in Hospital_details.objects.filter(type=typ)]
            #print(id_list)
            name_list=[obj.h_name for obj in Hospital_details.objects.filter(type=typ)]
            #print(name_list)
            type_list=[obj.type for obj in Hospital_details.objects.filter(type=typ)]
            #print(type_list)
            import requests


            for type,name,id,lat2,lon2 in zip(type_list,name_list,id_list,lat_list,long_list):
                  #def haversine(lon1, lat1, lon2, lat2):
                      """
                      Calculate the great circle distance between two points
                      on the earth (specified in decimal degrees).
                      Source: http://gis.stackexchange.com/a/56589/15183
                      """
                      try:
                          response = requests.get('http://www.google.com')
                      except:
                          print ('Can\'t connect to Google\'s server')
                          input('Press any key to exit.')
                          quit()

                        # use the Google Maps API
                      import googlemaps
                      gmaps = googlemaps.Client(key='AIzaSyAmQZOd607OVEzY34xdNjLkpJp_QgB0qRg')
                      origins = (lat1,lon1)
                      destinations = (lat2,lon2)
                      matrix = gmaps.distance_matrix(origins, destinations, mode='driving', language=None, avoid=None, units=None,
                                        departure_time=None, arrival_time=None,)
                      print (matrix)
                      dis=matrix["rows"][0]["elements"][0]["distance"]["text"]
                      dur=matrix["rows"][0]["elements"][0]["duration"]["text"]
                      addr=matrix["destination_addresses"]
                      print(dis)
                      print(dur)
                      #
                      # origins = (lat1,lon1)
                      # print(origins)
                      # destination = (lat2,lon2)
                      # print(destination)
                      #
                      # base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
                      # api_url = base_url+API_key
                      # json_response = requests.get(api_url,timeout=10).json()
                      #     #Check if your over your daily limit, if so try the next key
                      # # while json_response['status'] == 'OVER_QUERY_LIMIT':
                      # #       index += 1
                      # #        #if all keys used to max quotas, exit
                      # #       if index == len(key_list):
                      # #           atEnd = True
                      # #           break
                      # #       api_url = base_url + origin_part + destination_part + key_list[index]
                      # #       json_response = requests.get(api_url, timeout=10).json()
                      # print(json_response)
                      # dist = gmaps.distance_matrix(origins, destination, mode='driving')["rows"][0]["elements"][0]["distance"]["text"]
                      # time = gmaps.distance_matrix(origins, destination, mode='driving')["rows"][0]["elements"][0]["distance"]["text"]

                      #n_list.append(result)
                      # print(dist)
                      # print(time)

                      z=lat2
            #          print(lat2)
                      b=lon2
            #          print(lon2)

                      # convert decimal degrees to radians
                      # lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
                      # # haversine formula
                      # dlon = lon2 - lon1
                      # dlat = lat2 - lat1
                      # a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
                      # c = 2 * math.asin(math.sqrt(a))
                      # km = 6371 * c
                      list.append({'H_id':id,'name':name,'H_latitude':z,'H_longitude':b,'type':type,'distance':dis,'ETA':dur,'address':addr})
                  # #haversine()

                # lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
                # # haversine formula
                # dlon = lon2 - lon1
                # dlat = lat2 - lat1
                # a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
                # c = 2 * math.asin(math.sqrt(a))
                # km = 6367 * c
                # print(km)
                #
                # list.append(km)
                #print(list)

            return Response(list[:5])


class Hospital_details_UD(RetrieveUpdateDestroyAPIView):
    queryset=Hospital_details.objects.all()
    serializer_class=Hospital_details_Serializer
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object() # here the object is retrieved
    #     serializer = self.get_serializer(instance)
    #     return Response({'data':serializer.data,'status':True,'code':1001,'message':'Author Details'})
    #
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response({'data':serializer.data,'status':True,'code':1001,'message':'Author Details'})
    #
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
