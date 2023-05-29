from django.urls import path
from . import views


urlpatterns = [
    path('get_popular/', views.get_popular),
    path('get_first_four_categories/', views.get_first_four_categories),
    path('get_events_by_category/', views.get_events_by_category),
    path('get_all_categories/', views.get_all_categories),
    path('get_locations/', views.get_locations),
    path('get_events/', views.get_events),
    path('get_event/<int:event_id>/', views.get_event),
    path('get_event_features/<int:event_id>/', views.get_event_features),
    path('get_event_faq/<int:event_id>/', views.get_event_faq),
    path('get_vol_events/', views.get_vol_events),
    path('get_pos_shortlist/<int:event_id>/', views.get_pos_shortlist),
    path('get_pos_longlist/<int:event_id>/', views.get_pos_longlist),
    path('get_testimonials/<int:event_id>/', views.get_testimonials),
    path('signup/', views.signup),
    path('get_uni/', views.get_uni),
    path('login/', views.login),
    path('volunteer/', views.volunteer),
    path('post_rating/', views.post_rating),
    path('get_rating/', views.get_rating),

]