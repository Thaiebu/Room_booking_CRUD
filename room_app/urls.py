from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

from .views import PersonCreateView,PersonUpdateView,PersonListview,PersonDetailView,PersonDeleteView

urlpatterns =[
    # path("test/", views.testview,name="test"),
    # path("list/",views.list_room,name="list"),
    # path("list/<str:room_no>",views.get_room,name="room")

    path("",PersonCreateView.as_view()),
    path('person_update/<str:pk>', PersonUpdateView.as_view()),
    path('person_list/', PersonListview.as_view()),
    path('person_list/<pk>/', PersonDetailView.as_view()),
    path('person_list/<pk>/delete/',PersonDeleteView.as_view())

    # path("<pk:1>",PersonUpdateView.as_view(),name="update")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)