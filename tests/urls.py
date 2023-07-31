from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.urls import include, path, re_path


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('', include(auth_urls)),
    path('herald/', include('herald.urls')),
]
