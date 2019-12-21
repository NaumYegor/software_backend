from django.shortcuts import render, HttpResponse
import instagram
import json

account_name = 'student.nure'


def recent_photos(request):

    if request.method == 'GET':
        amount = request.GET["amount"]
        if not amount.isdigit():
            return HttpResponse("Amount's been entered in a wrong way.")
        else:
            links = []
            amount = int(amount)
            agent = instagram.WebAgent()
            account = instagram.Account(account_name)
            media, pointer = agent.get_media(account, count=amount)
            for content in media:
                link = 'https://www.instagram.com/p/{}/media/'.format(content)
                links.append(link)
            return HttpResponse(json.dumps(links))
    else:
        return HttpResponse("This method is not allowed.")
