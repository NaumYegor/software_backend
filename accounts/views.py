from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.mail import send_mail

from .models import Client

import random, string   # to generate random passwords

import json   # to convert data to json-response to AJAX-requests


def sign_in(request):
    if not(request.is_ajax() and request.method == 'POST'):
        print('NOT AJAX')
        if not request.user.is_authenticated:
            args = {}
            args.update(csrf(request))

            args['username'] = ''

            return render(request, 'accounts/login.html', args)
        else:
            return redirect('/')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            access = True
        else:
            access = False

        data = json.dumps(access)
        return HttpResponse(data, content_type='application/json')


def logout(request):
    auth.logout(request)
    return redirect('/')


def registration(request):
    if request.is_ajax():
        try:
            client = Client.objects.get(account=request.user)
            if client.status == 'u':
                return redirect('/')
        except:
            pass

        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email'].lower()
        status = request.POST['status']
        username = request.POST['username']
        password = request.POST['password']
        print(email)

        if request.user.is_authenticated:
            try:
                client = Client.objects.get(account=request.user)
                if client.status != 'a':
                    status = 'user'
            except:
                status = 'user'
        else:
            status = 'user'

        if len(User.objects.filter(username=username)) != 0:
            print('Existing username:', username)
            result = 'wrong_username'
            data = json.dumps(result)
            return HttpResponse(data, content_type='application/json')
        elif len(Client.objects.filter(email=email)) != 0:
            print('Existing email:', email)
            result = 'wrong_email'
            data = json.dumps(result)
            return HttpResponse(data, content_type = 'application/json')
        else:
            print('Registration allowed')
            html_message = f'Congratulations, {name}!<br><br>\
                             Somebody (probably you) registered you in our\
                             <a href = "https://127.0.0.1:8000/" style = "color: blue; text-decoration: none;">'\
                           f'small developing site</a><br><br>\
                             Your username: {username}<br>\
                             Your password: {password}<br><br>\
                             Enjoy!'
            send_mail('Account verification', 'Lol', 'Kek', [email], html_message=html_message)

            new_user = User.objects.create_user(username=username,
                                                password=password)
            if status == 'admin':
                new_user.is_staff = True
            new_user.save()

            if not request.user.is_authenticated:
                auth.login(request, new_user)

            new_client = Client(
                name=name,
                surname=surname,
                email=email,
                status=status[0],
                account=new_user
            )
            new_client.save()
                
            result = 'OK'
            data = json.dumps(result)
            return HttpResponse(data, content_type='application/json')
    else:
        args = {}
        args.update(csrf(request))

        if request.user.is_authenticated:
            args['username'] = request.user.username
        else:
            args['username'] = ''

        return render(request, 'accounts/registration.html', args)


def restore_password(request):
    if not request.is_ajax():
        args = {}

        if request.user.is_authenticated:
            return redirect('/')
        else:
            args['username'] = ''

        return render(request, 'accounts/restore_password.html', args)
    else:
        try:
            username = request.GET['username'].lower()
            if len(User.objects.filter(username=username)) == 0:
                success = False
                data = json.dumps(success)
                return HttpResponse(data, content_type='application/json')
            else:
                client = Client.objects.get(account=User.objects.get(username=username))
                email = client.email
                success = True
        except:
            email = request.GET['email'].lower()
            if len(Client.objects.filter(email=email)) == 0:
                success = False
                data = json.dumps(success)
                return HttpResponse(data, content_type='application/json')

        client = Client.objects.filter(email=email)[0]
        name = client.name
        user = client.account
        new_password = ''.join(random.choice(string.ascii_letters) for i in range(16))
        user.set_password(new_password)
        user.save()

        html_message = f'Hello, {name}!<br/><br/>' \
                       f'Your new password on our small developing site: {new_password}<br/><br/>Enjoy!'
        send_mail('Restoring password', 'Lol', 'Kek', [email], html_message=html_message)
        success = True
        data = json.dumps(success)
        return HttpResponse(data, content_type='application/json')
