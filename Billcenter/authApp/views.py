from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
import random

def user_login(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            email = loginform.cleaned_data['email']
            password = loginform.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                auth_login(request, user)

                # Get the next URL parameter or fallback to a default URL pattern name
                next_url = request.POST.get('next')  # No default value here
                if not next_url:  # If no 'next' URL is provided, default to a view name
                    next_url = reverse('dashboard:home')
                    
                    messages.success(request, f"Welcome {user.first_name}!")
                    return redirect(next_url)
            else:
                messages.error(request, "Incorrect email or password. Please try again.")
        else:
            messages.error(request, "Please correct the form errors.")

        # Render the login page again with the form and errors
        next_url = request.POST.get('next', '')
        return render(request, 'login.html', {'loginform': loginform, 'next': next_url})

    else:
        loginform = LoginForm()
        next_url = request.GET.get('next', '')

    form = RegisterForm()
    context = {
        'form': form,
        'loginform': loginform 
    }  
    return render(request, 'login.html', context)




def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            user = get_user_model().objects.get(email=email)

            # Generate OTP
            otp = str(random.randint(100000, 999999))

            # Save OTP in session
            request.session['otp'] = otp

            # Send OTP via email
            subject = 'Your OTP for Bill Center'
            message = f'Your OTP is: {otp}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return redirect('auth:verify_email', email=email)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

def email_verification(request, email):
    return render(request, 'email_verification.html', {'email': email})



def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otpcode')  # The form field is 'otpcode'
        email = request.POST.get('email')

        # Check if 'otp' exists in session
        if 'otp' in request.session:
            session_otp = request.session.get('otp')  # Retrieve OTP from session

            if session_otp == otp:  # Compare the OTP from the session with the one entered by the user
                user = get_user_model().objects.get(email=email)
                auth_login(request, user)  # Log the user in
                del request.session['otp']  # Remove OTP from session after successful verification
                return redirect('dashboard:home')  # Redirect to dashboard after successful verification
            else:
                messages.error(request, "Invalid OTP")
        else:
            messages.error(request, "OTP not found in session. Please request a new OTP.")
    
    return render(request, 'email_verification.html')


def resend_otp(request):
    email = request.GET.get('email')
    user = get_user_model().objects.get(email=email)
    otp = str(random.randint(100000, 999999))
    request.session['otp'] = otp

    subject = 'OTP Resent - Bill Center'
    message = f'Your new OTP is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

    return redirect('auth:verify_email', email=email)  # Redirect to the verification page


def logout_view(request):
    logout(request)
    return redirect('auth:login')