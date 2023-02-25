from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages,auth
from django.contrib.auth.models import UserManager
from home.models import NewUser
# Create your views here.

# class CustomUserManager(UserManager):
#     def create_user(self, username, name,email=None, password=None,):
#         return self._create_user(username,name, email, password)

    # def create_superuser(self, username, email=None, password=None):
    #     return self._create_user(username, email, password)

def index(request):
    if request.method=="POST":
        username=request.POST['username']
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if NewUser.objects.filter(username=username).exists():
                messages.error(request, "Username exists")
                return redirect("/")
            else:
                if NewUser.objects.filter(email=email).exists():
                    messages.error(request,"E-mail already exists")
                    return redirect("/")
                else:   
                    user=NewUser(username=username, first_name=name, email=email, password=password)
                    user.save()
                    messages.success(request, "Account created Succesfully")
                    return redirect('home')
        else:
            messages.error(request, "Password do not match!")
            return redirect("/")
    
    return render(request,"singup.html")

def home(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        if NewUser.objects.filter(username=username):
            if NewUser.objects.filter(password=password):
                return redirect("/indexx")
        # if user is not None:
        #     login(request, user)
        #     return redirect("/indexx")
        else:
        # Return an 'invalid login' error message.
            messages.error(request, "Can't login")
            return render(request,"home.html")
    
    return render(request,"home.html")

# def home(request):
#     if request.method=="POST":
#         username= request.POST.get('username')
#         password= request.POST.get('password')
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/indexx")
#         else:
#         # Return an 'invalid login' error message.
#             messages.error(request, "Can't login")
#             return render(request,"home.html")
    
#     return render(request,"home.html")

def indexx(request):
    return render(request,"index.html")





# def index(request):
#     # if request.user.is_anonymous:
#     #     return redirect("/singup")
#     if request.method=="POST":
#         username=request.POST['username']
#         raw_password=request.POST['password']
#         user=authenticate(username=username,password=raw_password)
#         user.save()
#         messages.success(request, "Succefully login")
#         return redirect('/singup')
#     return render(request,"home.html")
# def singup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             print(username)
#             return redirect('index.html')
#     else:
#         form = UserCreationForm()
#     return render(request, 'singup.html', {'form': form})
# def loginuser(request):
#     if request.method=="POST":
#         username= request.POST.get('username')
#         password= request.POST.get('password')
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#         # Return an 'invalid login' error message.
#             return render(request,"login.html")
#     return render(request,"login.html")
# def logoutuser(request):
#     logout(request)
#     return redirect("/login")