
from django.shortcuts import render


#from django.contrib import auth
from django.contrib.auth.models import User, auth

# Create your views here.

def signup(request):

    if request.method == "POST":
        
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        if username=="" or email=="" or password=="" or confirm_password=="":

            return render(request, 'signup.html',{'msg':"Please fill required field!"})

        
        if password != confirm_password:
            return render(request, 'signup.html',{'msg':'Password do not match!'})
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html',{'msg':'Username already Exists!'})

        else:
            if User.objects.filter(email=email).exists():
                return render(request, 'signup.html',{'msg':'Email already Exists!'})

            else:
                #Looks good
                #User.objects.create(first_name=fn, last_name = ln, username = username, password = password,email = email)
                user = User.objects.create_user(username = username, password = password,email = email)
                user.save()
                return render(request, 'login.html',{'msg':"Thanks for Registering with us."})

    else:
        return render(request,"signup.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'dashboard.html',{'msg':"You are now logged in"})
        else:
            return render(request, 'login.html', {'msg':"User does not exist!"} )
    else:
        return render(request,'login.html')   
    


def logout(request):
    
    auth.logout(request)
    return render(request, 'signup.html',{'msg':"Successfully logged out!"})


