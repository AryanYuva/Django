from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact
from math import ceil
# Create your views here.
def index(request):
    products = product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides,'range':range(1,nSlides),'product': products}
    allprods = []
    catprods = product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category= cat)
        n = len(products)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1,nSlides), nSlides])
    params = {'allprods':allprods}
    return render(request,'shop/index.html',params)
def about(request):
     return render(request,'shop/about.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        # print(name,email,phone,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')
def tracker(request):
     return render(request,'shop/tracker.html')
def search(request):
     return render(request,'shop/search.html')
def productView(request, myid):
    # Fetch the product using id 
     products = product.objects.filter(id=myid)
    #  print(products)
     return render(request,'shop/prodview.html',{'product':products[0]})
def Checkout(request):
      return render(request,'shop/checkout.html')
