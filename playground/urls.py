from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('dataquery/', views.data_query),
    path('ordereditems/', views.ordered_items)
]