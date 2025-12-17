from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserProfile,UserRole


def login_page(request):
    if request.method =="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=User.objects.get(email=email)
            if user.check_password(password):
                login(request,user)
                messages.success(request,'Logged in successfully!')
                try:
                    if user.role.role == 'admin':
                        return redirect('admin_dashboard_page')
                    elif user.role.role == 'vendor':
                        return redirect('vendor_dashboard_page')
                    elif user.role.role == 'farmer':
                        return redirect('farmer_dashboard_page')
                except Exception as e:
                    messages.error(request,f'Error {str(e)}')
                    return redirect('login_page')
        except User.DoesNotExist:
            messages.error(request,'Invalid email or password')
            return redirect('login_page')
            
        
        
        
    
    return render(request,'pages/login.html')

