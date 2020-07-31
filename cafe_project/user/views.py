from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import CustomUser



def sign_up(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        c_pwd = request.POST['check_password']

        if CustomUser.objects.filter(email=email).distinct() :
            return render(request, 'user/signUp.html',{'err': "중복 id존재"})

        if pwd != c_pwd :
            return render(request, 'user/signUp.html', {"err" : "암호가 일치하지 않아"})
        
        customuser =CustomUser(
            username = username,
            email = email
        )
        customuser.set_password(pwd)

        customuser.save()

        return redirect("home")    
    else :
         return render(request, 'user/signUp.html')

def login(request) :
    if request.method == 'POST' :
       email = request.POST['email']
       pwd = request.POST['password']

       user = get_object_or_404(CustomUser, email=email)

       if check_password(pwd, user.password) :
           request.session['user'] = user.username
           return redirect('home')
       else:
           return render(request, 'user/login.html', {"err": "패스워드입력"})
    else :
        
        return render(request, 'user/login.html')
        
def logout(request) :
    if request.session.get('user',False) :
        request.session.modified = True
        del request.session['user']
        return redirect('home')
    else :
        return redirect("home")