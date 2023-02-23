from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, "authentication/home.html")

def signup(request):
    #
    # if request.method == 'POST':
    #     Username = request.POST['Username']
    #     FirstName = request.POST['Firstname']
    #     LastName = request.POST['Lastname']
    #     Email = request.POST['Email']
    #     Phone = request.POST['Phone']
    #     Password = request.POST['Password']
    #     CPassword = request.POST['CPassword']
    #     myuser = User.objects.create_user()
    #

    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signout(request):
    pass
