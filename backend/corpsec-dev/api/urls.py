from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from activities.api import *
from .views import *

#router = routers.DefaultRouter()
#router.register(r'lead', DepartmentViewSet,basename='lead')
#router.register(r'activities', ActivityViewSet)
#router.register(r'responses', AResViewSet)

#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('show', intial_state)
]