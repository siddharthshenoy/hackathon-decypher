from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.

def labourer(request):
    if request.method == 'POST' :
        Name : request.POST['Name']
        Photo : request.POST['Photo']
        Skill : request.POST['Skill']
        Locality : request.POST['Locality']
        Username : request.POST['Username']
        Password1 : request.POST['Password']
        Password2 : request.POST['Password1']

        if Password1==Password2:
            if User.objects.filter(Username=Username).exists():
                print('Username Taken')
            else:
                user = User.objects.create_user(Name=Name, Skill=Skill, Locality=Locality, Username=Username, Password=Password1)
                user.save();
                print('User Created')
        
        else:
            print("Password Doesn't match..")


    else:
        return render(request,labourer.html)