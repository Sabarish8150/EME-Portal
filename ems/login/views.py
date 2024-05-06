from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def index(request):
    return render(request, 'index.html')

def home(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print("1")
            if user is not None:
                login(request, user)
                # Redirect to the home page.
                print("s") 
                return redirect(index) 
                # Redirect to the home page
            else:
                # Return an 'invalid login' error message.
                error_message = 'Invalid username or password.'
                
                return redirect(index)
        else:
            # Form is not valid, handle form errors.
            error_message = 'Form is not valid.'
            print("u") 
            return redirect(index)
    else:
        form = LoginForm()
        return render(request, 'home.html', {'form': form, 'error_message': error_message})
