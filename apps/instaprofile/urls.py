# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from apps.instaprofile import views

urlpatterns = [

    # The home page
    path('instaprofile/', views.osintgram, name='instaprofile'),

]
