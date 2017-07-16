from django.conf.urls import url

from .views import (
    entries_create_view,
    entries_list_view,
    entries_detail_view
    )

urlpatterns = [
    url(r'^create/$', entries_create_view, name='create'),
    url(r'^$', entries_list_view, name='list'),
    url(r'^(?P<id>\d+)/$', entries_detail_view, name='detail'), #passing keywork argument
]
