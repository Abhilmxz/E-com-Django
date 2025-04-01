from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import CustomerRegisterForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Customer
from django.views import View


# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')


class CategoryView(View):
    def get(self, request,val):
        product = Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html',locals())


class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())




class ProductDetail(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',locals())
    


def CustomerRegistrationView(View):
    def get(self, request):
        form=CustomerRegisterForm()
        return render(request, 'app/customerregistration.html',locals())

    def post(self, request):
        form=CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Successful')
        else:
            messages.warning(request,'Invalid Input')
        return render(request, 'app/customerregistration.html',locals())
    

class ProfileView(View):
    def get(self, request):
        form=CustomerRegisterForm()
        return render(request, 'app/profile.html',locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.User
            name = form.cleaned_data['first_name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode,state=state)
            reg.save()
            messages.success(request,'Congrats! Profile Updated Successfully')
        else:
            messages.warning(request,'Invalid Input')       
        return render(request, 'app/profile.html',locals())
    
    def Address(request):
      add = Customer.objects.filter(user=request.user)
      return render(request,'app/address.html',locals())
        
def updateAddress(View):
    def get(self, request,pk):
        form = CustomerProfileForm()
        return render(request,'app/updateAddress.html',locals())
    def post(self, request,pk):
        form = CustomerProfileForm(request.POST)
        return render(request,'app/updateAddress.html',locals())