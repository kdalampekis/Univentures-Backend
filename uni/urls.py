from django.urls import path
from . import views


urlpatterns = [
    path('get_popular/', views.get_popular),
    path('get_first_four_categories/', views.get_first_four_categories),
    path('get_events_by_category/', views.get_events_by_category),
    path('get_all_categories/', views.get_all_categories),
    path('get_locations/', views.get_locations),
    path('get_events/', views.get_events),





]