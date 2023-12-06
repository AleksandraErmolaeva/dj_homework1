from django.urls import path
from .views import *

urlpatterns = [
    path ('sensors/', SensorsView.as_view()),
    path ('sensors/<pk>/', SensorView.as_view()),
    path ('measurements/', MeasurementView.as_view())

]
