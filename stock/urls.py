# from django import path
from . import views
from django.urls import path
from stock.views import total, samsung, main, kakao, hyundai, naver, sk

app_name = 'stock'

urlpatterns = [
    # path('', display_graph, name='display_graph'),
    path('', main, name='main'),
    path('samsung/', samsung, name='samsung'),
    path('total/', total, name='total'),
    path('kakao/', kakao, name='kakao'),
    path('hyundai/', hyundai, name='hyundai'),
    path('naver/', naver, name='naver'),
    path('sk/', sk, name='sk'),

]