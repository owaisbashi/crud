from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    customers=Customer.objects.all()
    orders= Order.objects.all().order_by('-date_created')[:3]
    order_count=Order.objects.count()

    order_pending=Order.objects.filter(status='Pending').count()
    order_delivered=Order.objects.filter(status='Delivered').count()
    return render(request,'accounts/dashboard.html',context={'customers':customers,'orders':orders,'order_count':order_count,'order_pending':order_pending,'order_delivered':order_delivered})


    
def customer(request,pk_test):
    customer= Customer.objects.get(id=pk_test)

    orders=customer.order_set.all()
    order_count = orders.count()

    context={'customer':customer,'orders':orders,'order_count':order_count}
    return render(request,'accounts/customer.html',context=context)

def products(request):
    products= Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})

def create_order(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
    context={'form':form}

    return render(request,'accounts/create_order.html',context)


def update_order(request,pk):
    form=OrderForm()
    
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    print(request.method)

    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')

    
        

    return render(request,'accounts/create_order.html',context={'form':form})


def delete_order(request,pk):
    
    print('hello')

    print(request.method)
    order=Order.objects.get(id=pk)
    if request.method=='POST':

    
        print(order)
        order.delete()
        return redirect('/')        

     
    return render(request,'accounts/delete.html',context= {'item':order})
