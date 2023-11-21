from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Member

# Create your views here.
def home(request):
    members = Member.objects.all()

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been logged in!!")
            return redirect('home')
        else:
            messages.success(request, "Error Logging In!!")
            return redirect('home')
    else:
        return render(request, 'website/home.html', {'members': members})

    return render(request, 'website/home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, "Successfully Logged out!!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

def member_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        member_record = Member.objects.get(id=pk)
        return render(request, 'record.html', {'member_record': member_record})
    else:
        messages.success(request, "Must be logged in to view data!!")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        #delete record
        delete_record = Member.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Deletion Successful")
        return redirect('home')
    else:
        messages.success(request, "You Must be Logged In To delete a record")
        return redirect('home') 

def add_record(request):
    form = AddMemberForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Saved")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else: 
        messages.success(request, "Login Error!!")
        return redirect('home')