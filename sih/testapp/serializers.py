from rest_framework.serializers import ModelSerializer

from .models import User_details,User_location_details,Driver_details,Driver_location_details,Booking,Hospital_details

#
# class User_login_details_Serializer(ModelSerializer):
#
#     class Meta:
#         model=User_login_details
#         fields='__all__'
#         #fields=('u_name','login_status')


class User_location_details_Serializer(ModelSerializer):

    class Meta:
        model=User_location_details
        fields='__all__'

class User_details_Serializer(ModelSerializer):
    #user_desc=User_login_details_Serializer(read_only=True,many=False)
    # u_bookings    =User_details_Serializer(read_only=True,many=True)
    # d_bookings    =Driver_details_Serializer(read_only=True,many=True)
    loc_desc=User_location_details_Serializer(read_only=True,many=False)
    class Meta:
        model=User_details
        fields='__all__'



class Driver_location_details_Serializer(ModelSerializer):
    class Meta:
        model=Driver_location_details
        fields='__all__'


class Driver_details_Serializer(ModelSerializer):
    driver_desc=Driver_location_details_Serializer(read_only=True,many=False)
    class Meta:
        model=Driver_details
        fields='__all__'


class Booking_Serializer(ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'

class Hospital_details_Serializer(ModelSerializer):
    class Meta:
        model=Hospital_details
        fields='__all__'
