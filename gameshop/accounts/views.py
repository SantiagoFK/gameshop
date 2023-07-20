# Accounts App views

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            
            # Set chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            
            # Save the user object
            new_user.save()
            
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {'user_form': user_form })    
    
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


