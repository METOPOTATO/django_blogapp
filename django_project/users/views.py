from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!Now you are able to login')
            return redirect('login')
        else:
            messages.error(request, 'Form is not valid')
            return render(request,'users/register.html',{'form':form})
    else:
        messages.error(request, 'Cannot create this account!')
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html') 