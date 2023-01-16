from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from .forms import *
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
# Create your views here.


@login_required(login_url='login')
@admin_only
def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()

    total_customer = customer.count()
    total_order = order.count()

    order_pending = order.filter(status='pending').count()
    order_delivered = order.filter(status='Delivered').count()

    context = {'customer': customer, 'order': order, 'total_customer': total_customer,
               'total_order': total_order, 'order_pending': order_pending, 'order_delivered': order_delivered}
    return render(request, 'home.html', context)

#######################################################################


def products(request):
    product = Products.objects.all()
    # context={'customer':customer,'order':order}
    return render(request, 'product.html', {'product': product})

#######################################################################

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def user_data(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    order_count = order.count()
    myFilter = OrderFilter(request.GET, queryset=order)
    order = myFilter.qs

    context = {'customer': customer, 'order': order,
               'order_count': order_count, 'myFilter': myFilter}
    return render(request, 'customer.html', context)

#######################################################################

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_page(request):

    order = request.user.customer.order_set.all()
    order_count = order.count()
    total_order = order.count()
    data=request.user.customer.id

    
    order_pending = order.filter(status='pending').count()
    order_delivered = order.filter(status='Delivered').count()
    

    context = {'order': order, 'total_order': total_order,
               'order_pending': order_pending, 'order_delivered': order_delivered,'data':data}

    return render(request, 'user.html', context)

#######################################################################

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_acc(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    context = {'form': form}
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    return render(request, 'accounts.html', context)

#######################################################################

def create_order(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form=OrderForm()
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('userpage')

    context = {'formset': formset}
    return render(request, 'create_order.html', context)

#######################################################################

def Update_Order(request, pk):
    
    order = Order.objects.get(id=pk)

    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
           return HttpResponse("couldn't update file")
    context = {'form': form}
    return render(request, 'update.html', context)

#######################################################################

def Delete_Order(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('home')

    context = {'item': order}
    return render(request, 'delete.html', context)

#######################################################################

@unauthenticated_user
def Login_page(request):

    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}

    return render(request, 'login.html', context)

#######################################################################

@unauthenticated_user
def Register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            
            return redirect('login')

    context = {'form': form}

    return render(request, 'register.html', context)

#######################################################################

def LogoutUser(request):
    logout(request)
    return redirect('login')

