from django.urls import path
from django.contrib import admin
from ServisHoloAPI.views import registration_view, authorization_view, distance_view, workload_view

urlpatterns = [
    path('api/v1/registration', registration_view.registration),
    path('api/v1/authorization', authorization_view.authorization),
    path('api/v1/geoposition', distance_view.distance),
    path('api/v1/workload', workload_view.workload),
    path('admin', admin.site.urls),
]
