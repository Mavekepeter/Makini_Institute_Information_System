from django.shortcuts import render,redirect
from .forms import SubscribersForm,MailMessageForm
from .models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
                form.save()
                messages.success(request,'subscription successfull')
                return redirect('home-url')
        else:
            form = SubscribersForm()
            context = {"form":form}
            return render(request,)
