from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('dataquery/', views.data_query),
    path('ordereditems/', views.ordered_items),
    path('only/',views.get_only_objects),
    path('defer/',views.get_deferred_objects),
    path('play/',views.play),
]