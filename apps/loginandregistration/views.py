from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'loginandregistration/index.html')

def validation(request):
    if request.method == "POST":
        user = User.Usermgr.filter(email = request.POST['email'])
        if user:
            messages.add_message(request, messages.INFO, 'User already exists, please login!')
            return redirect('/')
        else:
            result = User.Usermgr.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
            if result[0] == True:
                request.session['user_id'] = result[1].id
                request.session['status'] = 'registered'
                return redirect('/welcome')
            else:
                error_msg = result[1]
                for i in range(len(error_msg)):
                    messages.add_message(request, messages.ERROR, error_msg[i])
                return redirect('/')
    else:
        return redirect('/')


def welcome(request):
    user =  User.Usermgr.filter(id=request.session['user_id'])
    first_name = user[0].first_name
    last_name = user[0].last_name
    #first_name = User.Usermgr.get(id=request.session['user_id']).first_name
    context = {
        'first_name': first_name,
        'last_name': last_name
    }
    return render(request, 'loginandregistration/welcome.html', context)

def login(request):
    if request.method == "POST":
        user = User.Usermgr.filter(email = request.POST['email'])
        if not user:
            messages.add_message(request, messages.INFO, 'User does not exist, please Register!')
            return redirect('/')
        else:
            result = User.Usermgr.login(request.POST['email'], request.POST['password'])
            i = User.Usermgr.filter(email = request.POST['email'])
            if result[0] == True:
                request.session['user_id'] = i[0].id
                request.session['status'] = 'log'
                return redirect('/welcome')
            else:
                error_msg = result[1]
                for i in range(len(error_msg)):
                    messages.add_message(request, messages.ERROR, error_msg[i])
                return redirect('/')
    return redirect('/')

def logout(request):
    request.session.pop('user_id')
    return redirect ('/')
    #i = User.Usermgr.filter(email = request.POST['email'])
    #request.session.pop('i[0]')
    #return redirect ('/')
