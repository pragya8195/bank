from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from .models import services


# Create your views here.
def home(request):
    service = services.objects.all()
    context = {
        'bank_list': service
    }
    return render(request, "home.html", context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('finalapp:abc')
        else:
            messages.info(request, "invalid credentials")
            return render(request, 'login.html')

    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                # messages.info(request, "username taken")
                return redirect('finalapp:register')

            else:
                user = User.objects.create_user(username=username, password=password)

                user.save();
                return redirect('finalapp:login')
                # print("user created")
        else:
            # message.info(request, "password not matching")
            return redirect('finalapp:register')
        return redirect('finalapp:home')
    return render(request, "register.html")





def abc(request):

    return render(request, 'abc.html')


def details(request):


    return render(request, 'details.html')



def final(request):
    return render(request, 'final.html')
