from django.contrib.staticfiles.views import serve
from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('handle_cloudpayments', handle_cloudpayments, name='handle_cloudpayments'),
    path('handle_insales', handle_insales, name='handle_insales'),
    path('handle_insales_tumi', handle_insales_tumi, name='handle_insales_tumi'),
    path('handle_insales_piquadro', handle_insales_piquadro, name='handle_insales_piquadro'),

]