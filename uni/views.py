from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Events, Categories
from django.db.models import Max
from django.db.models import Prefetch


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
            'img_src': event.img_src,
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
