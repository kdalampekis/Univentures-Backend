from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Events, Categories, EventsOrganization, EventsCategories, Features
from django.db.models import Max
from django.db.models import Prefetch
from django.core import serializers
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def get_popular(request):
    # Retrieve the four events with the highest rating
    highest_rated_events = Events.objects.annotate(max_rating=Max('rating')).order_by('-max_rating')[:4]

    # Serialize the events data
    serialized_events = []
    for event in highest_rated_events:
        serialized_events.append({
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'location': event.location,
            'price': event.price,
            'rating': event.rating,
            'imgSrc': event.img_src,
        })

    return Response(serialized_events)


@api_view(['GET'])
def get_first_four_categories(request):
    categories = Categories.objects.all()[:4]  # get the first 4 categories

    categories_dict = {}

    for category in categories:
        categories_dict[category.categ_name] = [
            {
                "id": category.id,
                "name": category.categ_name,
                "full": category.categ_apr,
                "desc": category.categ_desc,
            }
        ]

    return Response(categories_dict)


@api_view(['GET'])
def get_events_by_category(request):
    result = {}
    categories = Categories.objects.all()
    for category in categories:
        events = category.events_set.order_by('timestamp')[:2]  # Fetching events directly using related_name
        result[category.categ_name] = []
        for event in events:
            event_orgs = event.organizers.all()
            company = event_orgs[0].org_name if event_orgs else ''
            event_data = {
                'id': event.id,
                'name': event.title,
                'location': event.location,
                'date': event.timestamp.strftime('%d %B %Y'),
                'company': company,
                'imageSrc': event.img_src,
            }
            result[category.categ_name].append(event_data)

    return Response(result)


@api_view(['GET'])
def get_all_categories(request):
    categories = Categories.objects.all()

    categories_dict = []

    for category in categories:
        categories_dict.append({
                "value": category.categ_name,
                "label": category.categ_apr})

    return Response(categories_dict)


@api_view(['GET'])
def get_locations(request):
    events = Events.objects.all()
    locations_found = []
    events_locations = []

    for event in events:
        if event.location not in locations_found:
            events_locations.append(
                {
                    "value": event.location,
                    "label": event.location,
                }
            )
            locations_found.append(event.location)

    return Response(events_locations)


@api_view(['GET'])
def get_events(request):
    events = Events.objects.all()
    serialized_events = serializers.serialize('python', events)

    event_list = []
    for event_data in serialized_events:
        event = event_data['fields']
        event['id'] = event_data['pk']
        event_organizers = EventsOrganization.objects.filter(events=event_data['pk']).first()
        event['company'] = event_organizers.organization.org_name if event_organizers else None
        event_categories = EventsCategories.objects.filter(events=event_data['pk'])
        event['category'] = [categories.categories.categ_name for categories in event_categories]

        # Format the date
        timestamp = event['timestamp']
        formatted_date = timezone.localtime(timestamp).strftime('%d %b %Y')
        event['date'] = formatted_date

        # Include only specific fields
        modified_event = {
            'id': event['id'],
            'name': event['title'],
            'location': event['location'],
            'date': event['date'],
            'company': event['company'],
            'imageSrc': event['img_src'],
            'category': event['category'],
        }
        event_list.append(modified_event)

    return Response(event_list)


@api_view()
def get_event(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    serialized_event = serializers.serialize('python', [event]) # event is passed as list to make it iterable
    event_data = serialized_event[0] # We need to get the first object of serialized data because serialize returns a list
    event = event_data['fields']
    timestamp = event['timestamp']
    formatted_date = timezone.localtime(timestamp).strftime('%d %b %Y')
    event['date'] = formatted_date

    event_found = {
        'id': event_id,
        'imageSrc': event['img_src'],
        'title': event['title'],
        'description': event['description'],
        'location': event['location'],
        'pricingText': event['price'],
        'videoSrc': event['video_src'],
        'date':  event['date'],
        'price': event['price'],

    }
    return Response(event_found)

@api_view()
def get_event_features(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    features = Features.objects.filter(event=event)

    features_list = []

    for feature in features:
        features_data = {
            'key': feature.name,
            'value': feature.desc
        }
        features_list.append(features_data)

    return Response(features_list)