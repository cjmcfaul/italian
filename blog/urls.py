from django.conf.urls import url
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(
    r'^view_post/(?P<slug>[-\w]+)/',
    views.view_post,
    name='view_post'),

    url(
    r'^view_rating/(?P<rating_id>[0-9]+)/$',
    views.view_rating,
    name='view_rating'),

    url(
    r'^view_restaurant/(?P<name>[-\w]+)/',
    views.view_restaurant,
    name='view_restaurant'),

    url(r'^$', views.index, name='index'),

    url(r'^restaurants/$', views.restaurants, name='restaurants'),
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
