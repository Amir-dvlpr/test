from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User1
from first_app.forms import forms
 
from django.contrib.auth.decorators import login_required


def index(request):
    user_list =  User1.objects.order_by('first_name')
    user_dict = {'users':user_list,'title':'test'}
    return render(request, 'index.html', context= user_dict)    
 
def users(request):
    form = forms.newForm()
    if request.method == 'POST':
        form = forms.newForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('error')
    return render(request,'form.html',{'form':form})

    
def formshow(request):
    form = forms.formname()
   
    if request.method == 'POST':
        form = forms.formname(request.POST)
        if form.is_valid():
            print('valid')

    return render(request, 'form.html',{'form':form})
# Create your views here.


def register(request):

    register = False

    if request.method == "POST":
        userform = UserForm(data = request.POST)
        userprofile =  UserProfileInfos(data = request.P)