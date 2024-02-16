from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser as User
from .forms import CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        # check if email is provided
        if not email:
            # if email is not provided
            return render(request, 'register.html', {'error_message': 'Email is required'})

        # if user exit
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error_message': 'User with this email already exists'})

        # create new user
        user = User.objects.create_user(email=email, username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/') 
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
