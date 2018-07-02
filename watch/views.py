from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, HoodForm
from .emails import send_activation_email
from .tokens import account_activation_token
from .models import Profile, Hood

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    title = 'Hood-Watch'

    if request.method == 'POST':
        form = HoodForm(request.POST)
        if form.is_valid():
            geolocate = form.save(commit = False)
            geolocate.save()
        else:
            form = HoodForm()

    return render(request, 'index.html',{'form':HoodForm,'title':title})


# def signup(request):
#     if request.user.is_authenticated():
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             form = SignupForm(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 user.is_active = False
#                 user.save()
#                 current_site = get_current_site(request)
#                 to_email = form.cleaned_data.get('email')
#                 send_activation_email(user, current_site, to_email)
#                 return HttpResponse('Confirm your email address to complete registration')
#         else:
#             form = SignupForm()
#             return render(request, 'registration/signup.html',{'form':form})

    
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return HttpResponse('Thank you for confirming email. Now login to your account')
#     else:
#         return HttpResponse('Activation link is invalid')