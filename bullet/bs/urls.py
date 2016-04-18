from django.conf.urls import url, include
from django.contrib import admin

from .views import (
    bs_create,
    bs_show,
    bs_api,
    )

urlpatterns = [
    url(r'^create/$',bs_create),
    url(r'^show/$',bs_show),
    url(r'^api/$',bs_api.as_view()),
]
