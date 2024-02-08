from django.urls import path
from . import views as v

urlpatterns = [
    path('event-list/', v.event_list, name="event-list"),
    path('event-detail/<str:pk>', v.event_detail, name="event-detail"),
    path('event-create/', v.event_create, name="event-create"),
    path('event-update/<str:pk>', v.event_update, name="event_update"),
    path('event-delete/<str:pk>', v.event_delete, name="event_delete"),
]