from django.urls import path
from .views import LeadsCreateView, LeadsListView, LeadsFetchView


urlpatterns = [
    path("lead", LeadsCreateView.as_view(), name="Lead Create"),
    path("leads", LeadsListView.as_view(), name="Lead List"),
    path("get-lead", LeadsFetchView.as_view(), name="Lead Fetch"),


]