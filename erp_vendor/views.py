from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib import messages
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .serializers import VendorSerializer

def home(request):
    vendors = Vendor.objects.all()
    return render(request,'home.html',context={'vendors':vendors})


# vendor api
class vendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
#Vendor Page
def vendor_page(request):
    # fetching data 
    if request.method == "POST":
        vendor_id = request.POST.get('vendor_id')
        gst_number = request.POST.get('gst_number')
        city = request.POST.get('city')
        pan_number = request.POST.get('pan_number')
        vendor_name = request.POST.get('vendor_name')

        vendor_id = Vendor.objects.filter(vendor_id = vendor_id)
        if vendor_id.exists():
            messages.error(request,"Account already exists please login..!!")
            return redirect('/')
        vendor = Vendor.objects.create(
            vendor_id = vendor_id,
            gst_number = gst_number,
            pan_number = pan_number,
            vendor_name = vendor_name,
            city = city,
        )
        messages.success(request,"Data Saved")
        return redirect("/")

    return render(request,"vendor_erp.html")
    