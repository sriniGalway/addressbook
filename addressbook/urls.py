from django.conf.urls import url

from .views import (
    entries_create_view,
    entries_update_view,
    entries_list_view,
    entries_delete_view,
    entries_detail_view
    )

urlpatterns = [
    url(r'^$', entries_list_view, name='list'),
    url(r'^create/$', entries_create_view, name='create'),
    url(r'^(?P<id>\d+)/edit/$', entries_update_view, name='update'), #passing keywork argument
    url(r'^(?P<id>\d+)/delete/$', entries_delete_view, name='delete'), #passing keywork argument
    url(r'^(?P<id>\d+)/$', entries_detail_view, name='detail'), #passing keywork argument
]
