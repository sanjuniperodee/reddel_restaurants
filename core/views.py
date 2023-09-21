import csv
import json
import os
import hashlib
import uuid
from pathlib import Path
from django.core import serializers
from django.db.models import Q
import random
import string
import subprocess
import stripe
import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Restaurant, Certificate


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


@cors_headers(allow_origin="*", allow_methods="GET", allow_headers="*", allow_credentials=True)
def get_restaurants(request):
    data = []
    for i in Restaurant.objects.all():
        tags = []
        for tag in i.tags.all():
            tags+=tag.title
        item = {
            'id': i.pk,
            'title': i.title,
            'description': i.description,
            'tags': [tag.title for tag in i.tags.all()],
            'image': i.image.url,
            'slug': i.slug,
            'location': i.location,
            'kitchen': i.kitchen,
            'average': i.average,
            'phone': i.phone_number
        }
        data.append(item)
    return JsonResponse({
        "restaurants": data})
@cors_headers(allow_origin="*", allow_methods="GET", allow_headers="*", allow_credentials=True)
def get_restaurant_by_slug(request, slug):
    try:
        item = Restaurant.objects.get(slug=slug)
        data = {
            'id': item.pk,
            'title': item.title,
            'description': item.description,
            'tags': [tag.title for tag in item.tags.all()],
            'image': item.image.url,
            'prices': item.prices.split(','),
            'slug': item.slug,
            'location': item.location,
            'kitchen': item.kitchen,
            'average': item.average,
            'phone': item.phone_number,
            'prices': item.prices.split(',')
        }
        return JsonResponse({'data': data})
    except Restaurant.DoesNotExist:
        return JsonResponse({'error': 'Restaurant not found'}, status=404)


@cors_headers(allow_origin="*", allow_methods="GET", allow_headers="*", allow_credentials=True)
def get_new_restaurants(request):
    data = []
    for i in Restaurant.objects.all():
        tags = []
        for tag in i.tags.all():
            tags+=tag.title
        item = {
            'id': i.pk,
            'title': i.title,
            'description': i.description,
            'tags': [tag.title for tag in i.tags.all()],
            'image': i.image.url,
            'slug': i.slug,
            'location': i.location,
            'kitchen': i.kitchen,
            'average': i.average,
            'phone': i.phone_number
        }
        data.append(item)
    return JsonResponse({
        "restaurants": data})


@cors_headers(allow_origin="*", allow_methods="*", allow_headers="*", allow_credentials=True)
def create_certificate(request):
    try:
        # Get the raw request body data as bytes
        raw_data = request.body
        json_string = raw_data.decode('utf-8')
        data = json.loads(json_string)
        selected_price = data.get('price')
        print(data.get('price'))
        print(data.get('user_id'))
        certificate = Certificate(
            sum=data.get('price'),
            user_id=data.get('user_id')
        )
        certificate.save()
    except:
        print('error')
    return JsonResponse({'data': "exit"})


@cors_headers(allow_origin="*", allow_methods="GET", allow_headers="*", allow_credentials=True)
def get_certificates_by_id(request, id):
    data = []
    for i in Certificate.objects.filter(user_id=id):
        item = {
            'id': i.pk,
            'sum': i.sum,
            'user_id': i.user_id,
            'status': i.status,
        }
        data.append(item)
    return JsonResponse({"certificates": data})































stripe.api_key = settings.STRIPE_SECRET_KEY
