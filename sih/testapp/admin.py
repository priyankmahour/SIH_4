from django.contrib import admin

# Register your models here.

from .models import User_details,User_location_details,Driver_details,Driver_location_details,Booking,Hospital_details


class User_details_Admin(admin.ModelAdmin):
    list_display=['U_ID','mobile_no','f_name','l_name','email','token','user_status','created_at','update_at']

# class User_login_details_Admin(admin.ModelAdmin):
#     list_display=['DESC_ID','U_ID','login_status','login_time','logout_time']

class User_location_details_Admin(admin.ModelAdmin):
    list_display=['LOC_ID','U_ID','u_lattitude','u_longitude','update_time']

class Driver_details_Admin(admin.ModelAdmin):
    list_display=['D_ID','username','password','mobile_no','vehicle_no','availability']

class Driver_location_details_Admin(admin.ModelAdmin):
    list_display=['DLOC_ID','D_ID','u_lattitude','u_longitude','update_time']

class Booking_Admin(admin.ModelAdmin):
    list_display=['B_ID','U_ID','D_ID','des_latitude','des_longitude','booking_time']

class Hospital_details_Admin(admin.ModelAdmin):
    list_display=['H_ID','h_name','type','h_latitude','h_longitude']


admin.site.register(User_details,User_details_Admin)
#admin.site.register(User_login_details,User_login_details_Admin)
admin.site.register(User_location_details,User_location_details_Admin)
admin.site.register(Driver_details,Driver_details_Admin)
admin.site.register(Driver_location_details,Driver_location_details_Admin)
admin.site.register(Booking,Booking_Admin)
admin.site.register(Hospital_details,Hospital_details_Admin)
