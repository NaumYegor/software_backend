from django.shortcuts import render, HttpResponse


def home(request):
    args = {}

    if request.user.is_authenticated:
        args['username'] = request.user.username
    else:
        args['username'] = ''
    print(args)

    return render(request, 'main/home.html', args)
