from django.db import models

# Create your models here.

class User_details(models.Model):
    U_ID            =models.AutoField(primary_key=True)
    mobile_no       =models.CharField(max_length=10,blank=True)
    f_name          =models.CharField(max_length=12,blank=True)
    l_name          =models.CharField(max_length=12,blank=True)
    email           =models.EmailField(max_length=40,blank=True)
    token           =models.CharField(max_length=1000,blank=True)
    user_status     =models.BooleanField(default=True,blank=True)
    blood_type      =models.CharField(max_length=3,blank=True)
    created_at      =models.DateTimeField(auto_now_add=True)
    update_at       =models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return self.f_name


# class User_login_details(models.Model):
#     DESC_ID             =models.AutoField(primary_key=True)
#     U_ID                =models.OneToOneField(User_details,on_delete=models.CASCADE,related_name='user_desc')
#     login_status        =models.BooleanField(default=False)
#     login_time          =models.DateTimeField(auto_now_add=True,)
#     logout_time         =models.DateTimeField(auto_now_add=True,)




class User_location_details(models.Model):
    LOC_ID               =models.AutoField(primary_key=True)
    U_ID                 =models.OneToOneField(User_details,on_delete=models.CASCADE,related_name='loc_desc')
    u_lattitude          =models.FloatField(null=False,blank=True)
    u_longitude          =models.FloatField(null=False,blank=True)
    update_time          =models.DateTimeField(auto_now_add=True)

class Driver_details(models.Model):
    D_ID                 =models.AutoField(primary_key=True)
    username             =models.CharField(max_length=30,blank=True)
    password             =models.CharField(max_length=40,blank=True)
#   driver_status        =models.BooleanField(default=False,blank=True)
    mobile_no            =models.CharField(max_length=10,blank=True)
    vehicle_no           =models.CharField(max_length=10,blank=True)
    availability         =models.BooleanField(default=False,blank=True)
    def __str__(self):
         return self.username

class Driver_location_details(models.Model):
    DLOC_ID              =models.AutoField(primary_key=True)
    D_ID                 =models.OneToOneField(Driver_details,on_delete=models.CASCADE,related_name='driver_desc')
    u_lattitude          =models.FloatField(null=False,blank=True)
    u_longitude          =models.FloatField(null=False,blank=True)
    update_time          =models.DateTimeField(auto_now_add=True)


# class Driver_login_details(models.Model):
#     DLOG_ID              =models.AutoField(primary_key=True)
#     D_ID                 =models.OneToOneField(Driver_details,on_delete=models.CASCADE,related_name='driver_desc')
#     login_status         =models.BooleanField(default=False)
#     login_time           =models.DateTimeField(auto_now_add=True)
#     logout_time          =models.DateTimeField(auto_now_add=True)
#     availability         =models.BooleanField(default=False)


class Booking(models.Model):
    B_ID              =models.AutoField(primary_key=True)
    U_ID              =models.ForeignKey(User_details,on_delete=models.CASCADE,related_name='u_bookings')
    D_ID              =models.ForeignKey(Driver_details,on_delete=models.CASCADE,related_name='d_bookings')
    des_latitude      =models.FloatField(null=False,blank=True)
    des_longitude     =models.FloatField(null=False,blank=True)
    booking_time      =models.TimeField(auto_now_add=True,blank=True)
    #drop_time         =models.TimeField(auto_now_add=False,blank=True,null=True)



class Hospital_details(models.Model):
    H_ID              =models.AutoField(primary_key=True)
    h_name            =models.CharField(max_length=128,blank=True)
    type              =models.CharField(max_length=1,blank=True)
    h_latitude        =models.FloatField(null=False,blank=True)
    h_longitude       =models.FloatField(null=False,blank=True)
    distance          =models.CharField(max_length=128,blank=True)
    duration          =models.CharField(max_length=128,blank=True)
    def __str__(self):
        return self.h_name
