from django.shortcuts import render
from django.views.generic import CreateView,DetailView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
from django.http import HttpResponse

from django.views import View

from .forms import PostForm
from .models import Booking
from django.contrib.admin.widgets import AdminDateWidget


class PersonCreateView(CreateView):
    model = Booking
    fields = ('Room_No', 'Room_Type', 'Proof', 'photo','Name','Name_2','Address','Designation',
    'phone_number','Emergency_number','vehicel_number','Advance','Check_in_date','Check_out_date')
    template_name = 'index.html'
    success_url = 'person_list/'

    def get_form(self, form_class=None):
        form = super(PersonCreateView, self).get_form(form_class)
        form.fields['Check_in_date'].widget = AdminDateWidget(attrs={'type': 'date'})
        form.fields['Check_out_date'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form


 
class PersonListview(ListView):
    # specify the model to use
    model = Booking
    template_name = 'list_detail.html'
    ordering = ['Room_No']


class PersonUpdateView(UpdateView):
    model = Booking
    form_class = PostForm
    template_name = 'update-detail.html'
    success_url = 'http://127.0.0.1:8000/person_list/'
    def get_form(self, form_class=None):
        form = super(PersonUpdateView, self).get_form(form_class)
        form.fields['Check_in_date'].widget = AdminDateWidget(attrs={'type': 'date'})
        form.fields['Check_out_date'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form

class PersonDetailView(DetailView):
    model = Booking
    template_name = 'room_detail.html'

class PersonDeleteView(DeleteView):
    model = Booking
    template_name = 'delete_alert.html'
    success_url = 'http://127.0.0.1:8000/person_list/'


# def testview(request):
#     context = {}
#     context["form"] = PostForm()
#     return render(request, 'index.html', context)

# def list_room(request):
#     Rooms = Booking.objects.all()

#     context = {"Rooms":Rooms}
#     return render(request,'list_deatail.html',context)

# def get_room(request,room_no):
#     Room = Booking.objects.get(Room_No=room_no)

#     print(Room.Name)

#     context = {"Room":Room}
#     return render(request,'room_detail.html',context)




