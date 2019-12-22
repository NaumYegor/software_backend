from django.shortcuts import HttpResponse

import requests

from datetime import datetime

import json


def get_data():
    global last_check

    amount = 10
    data = {
        'student.nure': [],
        'i_nure': [],
        'senat.nure.ua': []
    }

    for inst in data:
        posts = json.loads(requests.get(f'https://www.instagram.com/{inst}/?__a=1').text)['graphql']['user']['edge_owner_to_timeline_media']\
                                                                                         ['edges'][:amount]
        for post in posts:
            post_code = post['node']['shortcode']
            data[inst].append(f'https://www.instagram.com/p/{post_code}/')

    return data

last_check = datetime.now()
data = get_data()

check_period = 300


def recent_photos(request):
    global data, last_check, check_period

    if (datetime.now() - last_check).seconds >= check_period:
        try:
            if request.method == 'GET':
                amount = int(request.GET['amount'])
            else:
                amount = int(request.POST['amount'])
        except:
            amount = 10
        
        data = get_data()
        last_check = datetime.now()

    data_to_return = json.dumps(data)
    return HttpResponse(data_to_return, content_type='application/json')
