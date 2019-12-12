from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            return HttpResponse('Username does not exits.')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            return HttpResponse('Authenticated')
        else:
            return HttpResponse('Invalid password')
    else:
        html = '<!DOCTYPE html>\
        <html>\
        <head>\
        <title></title>\
        </head>\
        <body>\
        <form action="" method="post">\
        <input type="text" name="username">\
        <input type="password" name="password">\
        <button type="submit" name="">Login</button>\
        </form>\
        </body>\
        </html>'
        return HttpResponse(html)
