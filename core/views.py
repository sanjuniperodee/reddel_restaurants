import json
import subprocess
import urllib
from django.shortcuts import render, get_object_or_404
import stripe
from django.conf import settings
from django.http import JsonResponse
import threading
import requests
import json

lock = threading.Lock()
condition = threading.Condition(lock)


def cors_headers(allow_origin="*", allow_methods="*", allow_headers="*", allow_credentials=True):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            response = view_func(request, *args, **kwargs)
            if isinstance(allow_origin, str):
                response["Access-Control-Allow-Origin"] = allow_origin
            elif isinstance(allow_origin, list):
                response["Access-Control-Allow-Origin"] = ", ".join(allow_origin)
            response["Access-Control-Allow-Methods"] = allow_methods
            response["Access-Control-Allow-Headers"] = allow_headers
            if allow_credentials:
                response["Access-Control-Allow-Credentials"] = "true"
            return response

        return wrapped_view

    return decorator

@cors_headers(allow_origin="*", allow_methods="*", allow_headers="*", allow_credentials=True)
def handle_cloudpayments(request):
    print(request.body)
    data = json.loads(request.body.decode('utf-8'))
    print([data.get('cvv'), data.get('cardNumber'), data.get('expDateMonth'), data.get('expDateYear')])
    output = subprocess.check_output(['node', 'core//js.js', data.get('cvv'), data.get('cardNumber'), data.get('expDateMonth'), data.get('expDateYear')], text=True)
    # print(output.strip())
    headers = {"Content-Type": "application/json",
               "Authorization": "Basic cGtfNmIwOTVjNzRmYTYxOWU2ZDc5ZGRlZTA2MzM3NWQ6MmZiNzczZjJkY2RjZjg2MGIxNzUxOWU4MmJlZjBiNzk="}
    response = requests.post("https://api.cloudpayments.ru/payments/cards/charge", headers=headers, json={'Amount': data.get('Amount'),
                                                                                                          'CardCryptogramPacket' : output.strip()})
    print(response.json())
    return JsonResponse(response.json())
    # return JsonResponse({'message': '200 OK'})


@cors_headers(allow_origin="*", allow_methods="*", allow_headers="*", allow_credentials=True)
def handle_insales(request):
    text = request.body.decode('utf-8')
    print(text)
    key_value_pairs = text.split('&')
    decoded_data = {}
    for pair in key_value_pairs:
        key, value = pair.split('=')
        decoded_value = urllib.parse.unquote(value)
        decoded_data[key] = decoded_value
    print(decoded_data)
    return render(request, 'payment.html', decoded_data)


@cors_headers(allow_origin="*", allow_methods="*", allow_headers="*", allow_credentials=True)
def handle_insales_tumi(request):
    text = request.body.decode('utf-8')
    print(text)
    key_value_pairs = text.split('&')
    decoded_data = {}
    for pair in key_value_pairs:
        key, value = pair.split('=')
        decoded_value = urllib.parse.unquote(value)
        decoded_data[key] = decoded_value
    print(decoded_data)
    return render(request, 'tumi.html', decoded_data)


@cors_headers(allow_origin="*", allow_methods="*", allow_headers="*", allow_credentials=True)
def handle_insales_piquadro(request):
    text = request.body.decode('utf-8')
    print(text)
    key_value_pairs = text.split('&')
    decoded_data = {}
    for pair in key_value_pairs:
        key, value = pair.split('=')
        decoded_value = urllib.parse.unquote(value)
        decoded_data[key] = decoded_value
    print(decoded_data)
    return render(request, 'piquadro.html', decoded_data)

stripe.api_key = settings.STRIPE_SECRET_KEY
