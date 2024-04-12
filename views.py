from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('success')
                else:
                    # Return a 'disabled account' error message
                    return render(request, 'disabled_account.html')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'invalid_login.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def success(request):
    return render(request, 'success.html')
