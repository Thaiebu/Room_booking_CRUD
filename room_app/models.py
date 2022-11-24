from django.db import models

# Create your models here.

CHOICES = [

    ("Male", "Male"),
    ("Female", "Female")
    
    ]

ROOM_CHOICES = [
    ("Single Room", "Single Room"),
    ("Full Room", "Full Room"),
    ("Sharing Room", "Sharing Room")

]



class demo(models.Model):
    Name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    last_modified = models.DateTimeField(auto_now_add = True)
    gender =  models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = '1'
        )
    date = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.Name
class Booking(models.Model):
    Room_No = models.CharField(max_length=5 ,primary_key=True)
    Room_Type = models.CharField(
        max_length = 20,
        choices = ROOM_CHOICES,
        default = '1'
        )
    Proof = models.ImageField(upload_to = "proofs")
    photo = models.ImageField(upload_to = "photos")
    Name = models.CharField(max_length=100)
    Name_2 = models.CharField(max_length=100,blank=True)
    Address = models.TextField(blank=True)
    Designation = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=12,blank=True)
    Emergency_number = models.CharField(max_length=12,blank=True)
    vehicel_number = models.CharField(max_length=12,blank=True)
    Advance = models.CharField(max_length=10,blank=True)
    Check_in_date = models.DateTimeField(blank=True,null=True)
    Check_out_date = models.DateTimeField(blank=True,null=True)

    








