from django.contrib import admin
from .models import demo,Booking
# Register your models here.


# class BookAdmin(admin.ModelAdmin):
#     list_display = ('id', 'Name', 'gender')

# admin.site.register(demo,BookAdmin)

class BookRoom(admin.ModelAdmin):
    list_display = ('Room_No', 'Room_Type', 'Name','Name_2','Address','phone_number')

admin.site.register(Booking,BookRoom)

