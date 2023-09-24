import json
import stripe
from django.conf import settings
from django.http import JsonResponse
from .models import Restaurant, Certificate, Otklik, Order


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
        raw_data = request.body
        json_string = raw_data.decode('utf-8')
        data = json.loads(json_string)
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


@cors_headers(allow_origin="*", allow_methods="GET", allow_headers="*", allow_credentials=True)
def get_jobs_by_id(request, id):
    data = []
    for i in Order.objects.filter(user_id=id):
        tags = []
        for tag in i.otkliki.all():
            tags += {
                'user_id': tag.user,
                'price': tag.price,
                'description': tag.description,
            }
        item = {
            'id': i.pk,
            'price': i.price,
            'user_id': i.user_id,
            'content_work': i.title,
            'description': i.description,
            'company': i.company,
            'location': i.location,
            'category_id': i.category_id,
            'subcategory_id': i.subcategory,
            'experience': i.experience,
            'skills': i.skills,
            'otkliki': tags,
            'image': i.image.url
        }
        data.append(item)
    return JsonResponse({"data": data})


@cors_headers(allow_origin="*", allow_methods="GET", allow_headers="*", allow_credentials=True)
def get_job_by_id(request, id):
    i = Order.objects.filter(id=id)[0]
    tags = []
    for tag in i.otkliki.all():
        tags.append({
            'user_id': tag.user,
            'price': tag.price,
            'description': tag.description,
        })
    item = {
        'id': i.pk,
        'price': i.price,
        'user_id': i.user_id,
        'content_work': i.title,
        'description': i.description,
        'company': i.company,
        'location': i.location,
        'category_id': i.category_id,
        'subcategory_id': i.subcategory,
        'experience': i.experience,
        'skills': i.skills,
        'otkliki': tags,
    }
    if i.image:
        item['image'] = i.image.url;
    return JsonResponse({"data": item})


@cors_headers(allow_origin="*", allow_methods="GET", allow_headers="*", allow_credentials=True)
def get_jobs(request):
    data = []
    for i in Order.objects.all():
        tags = []
        for tag in i.otkliki.all():
            tags += {
                'user_id': tag.user,
                'price': tag.price,
                'description': tag.description,
            }
        item = {
            'id': i.pk,
            'price': i.price,
            'user_id': i.user_id,
            'content_work': i.title,
            'description': i.description,
            'company': i.company,
            'location': i.location,
            'category_id': i.category_id,
            'subcategory_id': i.subcategory,
            'experience': i.experience,
            'skills': i.skills,
            'otkliki': tags,
        }
        if i.image:
            item['image'] = i.image.url;
        data.append(item)
    return JsonResponse({"data": data})

@cors_headers(allow_origin="*", allow_methods="POST", allow_headers="*", allow_credentials=True)
def otklik(request, id):
    raw_data = request.body
    json_string = raw_data.decode('utf-8')
    data = json.loads(json_string)
    otklik = Otklik(
        user=data.get('userId'),
        price=data.get('price'),
        description=data.get('description'),
    )
    otklik.save()
    job = Order.objects.filter(pk=id)[0]
    job.otklik.add(otklik)
    job.save()
    return JsonResponse({"certificates": 'true'})


@cors_headers(allow_origin="*", allow_methods="*", allow_headers="*", allow_credentials=True)
def add_otklick(request, jobId, userId, description, price):
    job = Order.objects.filter(pk=jobId)[0]
    otklik = Otklik(
        price=price,
        description=description,
        user=userId
    )
    otklik.save()
    job.otkliki.add(otklik)
    return JsonResponse({'response': "200 OK"})

@cors_headers(allow_origin="*", allow_methods="*", allow_headers="*", allow_credentials=True)
def save_job(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        print(data.get('price'))
        order = Order(
            description=data.get('description'),
            company=data.get('company'),
            title=data.get('content_work'),
            experience=data.get('experience'),
            skills=data.get('experience'),
            price=data.get('price'),
            user_id=data.get('user_id'),
            category_id=data.get('category_id'),
            subcategory=data.get('subcategory_id'),
            location=data.get('location'),
        )
        order.save()

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", str(e))
    return JsonResponse({'error': 'Invalid JSON data'}, status=200)





























stripe.api_key = settings.STRIPE_SECRET_KEY
