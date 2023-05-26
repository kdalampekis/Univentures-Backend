from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Events, Categories, EventsOrganization, EventsCategories, Features, Faq, Postitions, Testimonials, Volunteer
from django.db.models import Max
from django.core import serializers
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import random

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


@api_view()
def get_event_faq(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    faqs = Faq.objects.filter(event=event)

    faqs_list = []

    for faq in faqs:
        features_data = {
            'question': faq.question,
            'answer': faq.answer
        }
        faqs_list.append(features_data)

    return Response(faqs_list)

@api_view(['GET'])
def get_vol_events(request):
    events = Events.objects.all()[:5]
    serialized_events = serializers.serialize('python', events)

    event_list = []
    for event_data in serialized_events:
        event = event_data['fields']
        event['id'] = event_data['pk']
        event_categories = EventsCategories.objects.filter(events=event_data['pk'])
        event['category'] = [categories.categories.categ_apr for categories in event_categories]
        modified_event = {
            'id': event['id'],
            'title': event['title'],
            'description': event['description'],
            'imageSrc': event['img_src'],
            'subtitle': event['category'],
        }
        event_list.append(modified_event)

    return Response(event_list)


@api_view()
def get_pos_shortlist(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    positions = Postitions.objects.filter(event=event).all()[:6]

    pos_list = []

    for position in positions:
        pos_data = {
            'value': position.pos_name,
            'label': position.pos_name
        }
        pos_list.append(pos_data)

    return Response(pos_list)

@api_view()
def get_pos_longlist(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    positions = Postitions.objects.filter(event=event).all()[:6]

    pos_list = []

    for position in positions:
        pos_data = {
            'title': position.pos_name,
            'description': position.pos_description,
            'imageSrc': position.pos_img,
        }
        pos_list.append(pos_data)

    return Response(pos_list)



@api_view(['GET'])
def get_testimonials(request, event_id):
    try:
        # Get all volunteer positions related to the event
        positions = Postitions.objects.filter(event__id=event_id)

        # Get all volunteers for these positions
        volunteers = Volunteer.objects.filter(position__in=positions)


        # Get all testimonials related to these volunteers
        testimonials = Testimonials.objects.filter(volunteer__in=volunteers)



        # Ensure we have at least 2 testimonials
        if testimonials.count() < 2:
            return Response({"message": "Not enough testimonials found for this event"}, status=404)

        # Select two random testimonials
        selected_testimonials = random.sample(list(testimonials), 2)

        result = []
        for testimonial in selected_testimonials:
            user = testimonial.volunteer.user
            position = testimonial.volunteer.position
            result.append({
                "profileImageSrc": user.img_src,
                "heading": testimonial.comment_title,
                "quote": testimonial.comment,
                "customerName": f"{user.first_name} {user.last_name}",
                "customerTitle": position.pos_name,
            })

        return Response(result, status=200)

    except ObjectDoesNotExist:
        return Response({"message": "No testimonials found for this event"}, status=404)

    except ValueError:
        return Response({"message": "An error occurred while processing the request"}, status=500)
