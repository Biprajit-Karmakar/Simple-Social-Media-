from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration_func(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "accounts/registration.html", {
        "form": form
    })

def login_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "accounts/login.html")

def logout_func(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def profile(request):
    profile = request.user.profile

    return render(request, 'account/profile.html',{
        'profile':profile
    })
