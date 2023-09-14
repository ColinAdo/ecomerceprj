from django.shortcuts import render, redirect
from .forms import RegisrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser


def register_view(request):
    template = 'userauths/sign-up.html'
    if request.method == 'POST':
        form = RegisrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} created successfully")

            new_user = authenticate(
                username=form.cleaned_data.get('username'), 
                password1=form.cleaned_data.get('password1'),
                )
            login(request, new_user)
            return redirect('home')

    else:
        form = RegisrationForm()


    context = {
        'form': form,
    }
    return render(request, template, context)

def login_view(request):
    template = 'userauths/sign-in.html'

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Login successful for {email}, welcome!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('signin')
        
    context = {}
    return render(request, template, context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('signin')