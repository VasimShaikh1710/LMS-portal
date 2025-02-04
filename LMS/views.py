from django.shortcuts import render, redirect
from .models import Phnuser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.urls import reverse




# Create your views here.
def home(request):
    if 'username' in request.session:
        username_initial = request.session['username'][0].upper()
        return render(request, 'home.html', {'username_initial': username_initial, 'is_logged_in': True})
    else:
        return render(request, 'home.html', {'is_logged_in': False})



from django.shortcuts import redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Fetch the user based on the username
            user = Phnuser.objects.get(username=username)
        except Phnuser.DoesNotExist:
            # If username is invalid, show error
            return render(request, 'login.html', {'error': 'Invalid username or password!'})

        # Now that we have the user, we can check the password
        if check_password(password, user.password):  # Checking if password matches
            # If password is correct, set the session and login
            request.session['username'] = user.username
            messages.success(request, 'Login successful!')
            # Get the next page to redirect to after login, or home if none is specified
            next_page = request.GET.get('next', 'home')
            return redirect(next_page)
        else:
            # If password is incorrect, show the error
            return render(request, 'login.html', {'error': 'Invalid username or password!'})

    return render(request, 'login.html')


def logout(request):
    if 'username' in request.session:
        del request.session['username']  # Clear the session
    return redirect('home')  # Redirect to home after logout


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])

        if Phnuser.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists!'})

        
        user = Phnuser(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'signup.html')


def qrscan(request):
    username = request.session.get('username')
    if username:
        return render(request, 'qrscan.html')
    else:
        return redirect('login')


def bionic_hand(request):
    username = request.session.get('username')
    if username:
        if 'username' in request.session:
            username_initial = request.session['username'][0].upper()
            return render(request, 'bionic_hand.html', {'username_initial': username_initial, 'is_logged_in': True})
    else:
        return redirect(f'{reverse("login")}?next={request.path}')


def home1(request):
    return render(request, 'home1.html')

def buybionicpage(request):
    return render(request, 'buybionicpage.html')




@login_required
def profile(request):
    user = request.user
    initials = get_initials(user)
    return render(request, 'bionic_hand.html', {'initials': initials})

def get_initials(user):
    # Assuming user has first_name and last_name fields
    name = user.get_full_name()
    initials = ''.join([part[0].upper() for part in name.split() if part])
    if not initials:  # In case the name is empty
        initials = user.username[0].upper()
    return initials




def base(request):
    if 'username' in request.session:
        username_initial = request.session['username'][0].upper()
        return render(request, 'base.html', {'username_initial': username_initial, 'is_logged_in': True})
    else:
        return render(request, 'base.html', {'is_logged_in': False})


def profile(request):
    return render(request, 'profile.html')


####################### OpenAI API ########################




def chat(request):
    return render(request, 'chat.html')

