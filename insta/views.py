from django.shortcuts import render, HttpResponse
import instagram
import json
import datetime as dt

account_name = 'student.nure'
update_period = 300
links = list()
last_stamp = dt.datetime.now().timestamp()-update_period


def recent_photos(request):

    if request.method == 'GET':
        global links
        global last_stamp

        if dt.datetime.now().timestamp()-last_stamp < update_period:
            return HttpResponse(json.dumps(links))
        else:
            links = []

        amount = request.GET.get("amount")
        if amount is None or not amount.isdigit():
            return HttpResponse("Amount's been entered in a wrong way.")
        else:
            amount = int(amount)
            agent = instagram.WebAgent()
            account = instagram.Account(account_name)
            media, pointer = agent.get_media(account, count=amount)
            for content in media:
                link = 'https://www.instagram.com/p/{}/media/'.format(content)
                links.append(link)
            last_stamp = dt.datetime.now().timestamp()
            return HttpResponse(json.dumps(links))
    else:
        return HttpResponse("This method is not allowed.")
