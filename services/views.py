from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib import messages
from .models import Product
from .credentials import *


# Create your views here.

def add_course(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The course ahs been saved successfully')
            return redirect('add_course-url')
        else:
            messages.error(request, 'course saving failed')
            return redirect('add_course-url')
    else:
        form = ProductForm
        return render(request, 'service/add_course.html', {"form": form})


def Buy_course(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        phone = request.POST['phone']
        amount = product.price
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "PYMENT001",
            "TransactionDesc": "School fees"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Your Payment Request Was Successful")
    return render(request, 'service/Buy_course.html', {"product": product})


def products(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, 'service/view_courses.html', context)


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('views_course-url')
