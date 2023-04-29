from django.shortcuts import render
from django.http import HttpResponse

Tax_Rate = 15

# Create your views here.
def wep (request):
    return render(request,"Taxes/temp1.html")
def Cal (request , num):
    num = num + (num * (Tax_Rate/100))
    return HttpResponse(num)
def taxerate(request):
    return render(request,"Taxes/temp3.html",{"Tax_Rate":Tax_Rate})