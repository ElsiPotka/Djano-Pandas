from django.urls import path
from . import views

urlpatterns = [
    path("sales-data/", views.sales_data_view, name="sales_data"),
]
