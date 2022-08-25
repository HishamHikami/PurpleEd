# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path("", admin.site.urls),          # Django admin route
   # path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    # path("", include("apps.home.urls"))
]

admin.site.site_title = "Site Title"
admin.site.site_header = "Site Header"
admin.site.index_title = "Index Title"