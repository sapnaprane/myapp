from django.contrib import admin
from django.urls import path
# importing views from views..py
from .views import p4n_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('time/',p4n_view),
    path('hello/', p4n_view, name='p4n_view')
]
