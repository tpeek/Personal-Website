from django.conf.urls import include, url
from django.contrib import admin
from .views import home_view, projects_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view, name='home'),
    url(r'^projects/', projects_view, name='projects'),
]
