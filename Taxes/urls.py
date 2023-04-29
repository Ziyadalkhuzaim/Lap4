from django.urls import path 
from.import views
urlpatterns = [
    path("",views.wep,name="TAX"),
    path("<int:num>",views.Cal,name="TAX"),
    path("taxrate",views.taxerate,name="TaxRate")
]