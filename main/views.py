from django.shortcuts import render, HttpResponse


def home(request):
    args = {}

    if request.user.is_authenticated:
        args['username'] = request.user.username
    else:
        args['username'] = ''

    print(args['username'])

    return render(request, 'main/home.html', args)


def company_info(request):
    args = {}

    if request.user.is_authenticated:
        args['username'] = request.user.username
    else:
        args['username'] = ''

    return render(request, 'main/company_info.html')


def edu_info(request):
    args = {}

    if request.user.is_authenticated:
        args['username'] = request.user.username
    else:
        args['username'] = ''

    return render(request, 'main/edu_plan.html')


def our_team(request):
    args = {}

    if request.user.is_authenticated:
        args['username'] = request.user.username
    else:
        args['username'] = ''

    return render(request, 'main/OurTeam/OurTeam.html')
