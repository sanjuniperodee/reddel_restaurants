from django.contrib.staticfiles.views import serve
from django.urls import path, re_path
from .views import *

app_name = 'core'

urlpatterns = [
    path('getAllRestaurants', get_restaurants, name='get_restaurants'),
    path('get_restaurant_by_slug/<slug>', get_restaurant_by_slug, name='get_restaurant_by_slug'),
    path('create_certificate', create_certificate, name='create_certificate'),
    path('get_certificates_by_id/<id>', get_certificates_by_id, name='get_certificates_by_id'),
    path('otklik/<id>', otklik, name='otklik'),
    path('get_jobs', get_jobs, name='get_jobs'),
    path('get_jobs_by_id/<id>', get_jobs_by_id, name='get_jobs_by_id'),
    path('get_job_by_id/<id>', get_job_by_id, name='get_job_by_id'),
    path('add_otklick/<jobId>/<userId>/<description>/<price>', add_otklick, name='add_otklick')
    # path('add_to_user_favourite/<userId>/<restaurantId>', add_to_user_favourite, name='add_to_user_favourite')
]