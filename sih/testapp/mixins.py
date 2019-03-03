import json
from django.core.serializers import serialize

from .models import User_details,User_location_details,Driver_details,Driver_location_details,Booking,Hospital_details

class SerializeMixin(object):
    def myserialize(self,qs):
        resp=serialize('json',qs)
        p_data=json.loads(resp)
        username_list=[]
        for obj in p_data:
            data=obj['fields']['username']
            username_list.append(data)
        #resp=json.dumps(final_list)
        return username_list

class SerializeMixin1(object):
    def myserialize1(self,qs,username):
        resp=serialize('json',qs)
        p_data=json.loads(resp)
        # id_list=[]
        # username_list=[]
        my_dict={}
        new_list=[]
        for obj in p_data:
            if obj['fields']['username']==username:
                id=obj['pk']
#             data=obj['pk']
# #            id_list.append(data)
#             my_dict["id"]=data
#             data1=obj['fields']['username']
# #            username_list.append(data1)
#             my_dict["username"]=data1
#             new_list.append(my_dict)
#             print(my_dict)
#         print("Hello")
#         print(new_list)
        return id
