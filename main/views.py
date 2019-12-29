from django.shortcuts import render, HttpResponse, redirect

from main.models import Article


def home(request):
    args = {}

    args['head_articles'] = Article.objects.all()[:3]
    args['articles'] = Article.objects.all()[3:]
    print(len(args['articles']))

    if request.user.is_authenticated:
        args['username'] = request.user.username
    else:
        args['username'] = ''

    return render(request, 'main/home.html', args)


def article(request, article_id):
    articles = Article.objects.filter(id = article_id)

    if len(articles) == 0:
        return redirect('/')

    args = {}
    args['article'] = articles[0]
    args['articles'] = Article.objects.all()

    return render(request, 'main/news.html', args)


def our_team(request):
    args = {}

    if request.user.is_authenticated:
        args['username'] = request.user.username
    else:
        args['username'] = ''

    return render(request, 'main/OurTeam/OurTeam.html')


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
