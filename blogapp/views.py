from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from .forms import CreateUserForm


def HomeView(request):
    return render(request, 'blogapp/home.html')


def AboutView(request):
    return render(request, 'blogapp/about.html')


def WelcomeView(request):
    return render(request, 'blogapp/welcome.html')


def ContactView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully !')
        return redirect('contact')
    context = {'form': form}
    return render(request, 'blogapp/contact.html', context)


def NewblogView(request):
    form = NewblogForm()
    if request.method == 'POST':
        form = NewblogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your blog has been created successfully !')
        return redirect('newblog')
    context = {'form': form}
    return render(request, 'blogapp/newblog.html', context)


def ShowblogView(request):
    blog = Newblog.objects.all()
    context = {'blog': blog}
    return render(request, 'blogapp/showblog.html', context)


@login_required(login_url='signin')
def UpdateView(request, id):
    # dictionary for initial data with field names as keys
    # fetch the object related to passed id
    blog = get_object_or_404(Newblog, id=id)
    form = NewblogForm(instance=blog)
    if(request.method == 'POST'):
        form = NewblogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your blog has been updated successfully !')
        return redirect('showblog')
    context = {'form': form}
    return render(request, 'blogapp/update.html', context)


@login_required(login_url='signin')
def DeleteView(request, id):
    # fetch the object related to passed id
    blog = get_object_or_404(Newblog, id=id)
    if request.method == "POST":
        # delete object
        blog.delete()
        messages.success(
            request, 'Your blog has been deleted successfully !')
        return redirect("showblog")
    context = {}
    return render(request, "blogapp/delete.html", context)


def SignupView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was Created for ' + user)

                return redirect('signin')

        context = {'form': form}
        return render(request, 'blogapp/signup.html', context)


def SigninView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('welcome')
            else:
                messages.info(request, 'Username Or Password is Incorrect')

        context = {}
        return render(request, 'blogapp/signin.html', context)


def SignoutView(request):
    logout(request)
    return redirect('signin')
