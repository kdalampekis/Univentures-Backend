from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Events, Categories, EventsOrganization, \
    EventsCategories, Features, Faq, Postitions, Testimonials, Volunteer, User, University, EventsUser
from django.db.models import Max
from django.core import serializers
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import random
from .serializers import UserSerializer, UsersCategoriesSerializer, VolunteerSerializer
from rest_framework import status
from recommend import m


@api_view(['POST'])
def get_popular(request):
    try:
        user_id = request.data['user_id']
        user = User.objects.get(pk=user_id)
        recommended = m(user.id)
        print(recommended)
        serialized_events = []
        for event_id in recommended:
            event = Events.objects.get(pk=event_id)
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
    except:
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
    positions = Postitions.objects.filter(event=event).all()

    pos_list = []

    for position in positions:
        if position.id < 50:
            pos_data = {
                'value': position.pos_name,
                'label': position.pos_name
            }
            pos_list.append(pos_data)

    return Response(pos_list)

@api_view()
def get_pos_longlist(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    positions = Postitions.objects.filter(event=event).all()

    pos_list = []

    for position in positions:
        if position.id < 50:
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
            if testimonial.volunteer.status == 'S':
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


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if User.objects.filter(email=request.data['email']).exists():
        return Response({'message': 'A user with this email already exists.'}, status=200)

    if serializer.is_valid():
        # Hash the user's password
        password = serializer.validated_data.get('password')
        serializer.validated_data['password'] = password

        uni = request.data.get('uni', [])
        university = University.objects.get(pk=uni['id'])
        serializer.validated_data['university'] = university

        serializer.save()

        category_names = request.data.get('categories', [])

        for category_name in category_names:
            category = Categories.objects.get(categ_name=category_name['value'])
            user = User.objects.get(email=request.data['email'])

            category_data = {
                'user': user.id,
                'categories': category.id
            }

            category_serializer = UsersCategoriesSerializer(data=category_data)

            if category_serializer.is_valid():
                category_serializer.save()
            else:
                return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_uni(request):
    unis = University.objects.all()
    university = []

    for uni in unis:
        university.append(
            {
                "id": uni.id,
                "value": uni.uni_name,
                "label": uni.uni_name,

            }
            )

    return Response(university)


@api_view(['POST'])
def login(request):

    if User.objects.filter(email=request.data['email']).exists():

        user = User.objects.get(email=request.data['email'])

        if user.email == request.data['email']:
            if user.password == request.data['password']:
                return Response({'message': 'Success', 'id': user.id}, status=200)
            else:
                return Response({'message': 'Incorrect password'}, status=500)
    else:
        return Response({'message': 'User doesnt exist'}, status=500)


@api_view(['POST'])
def volunteer(request):

    position_names = request.data.get('selectedVolOptions', [])

    for pos_name in position_names:
        position = Postitions.objects.get(pos_name=pos_name['value'])
        user = User.objects.get(pk=request.data['user_id'])
        comment = request.data['message']

        volunteer_data = {
        'position': position.id,
        'user': user.id,
        'comment': comment
        }

        vol_serializer = VolunteerSerializer(data=volunteer_data)

        if vol_serializer.is_valid():
            vol_serializer.save()
        else:
            return Response(vol_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Received'}, status=200)


@api_view(['POST'])
def post_rating(request):
    # Get the data from the request
    user_id = request.data.get('user_id')
    event_id = request.data.get('event_id')
    rating = request.data.get('rating')

    # Validate the data
    if not all([user_id, event_id, rating]):
        return Response({'message': 'Missing data in request'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Try to get the user and event instances
        user = User.objects.get(pk=user_id)
        event = Events.objects.get(pk=event_id)

        # Get or create the EventsUser object
        event_user, created = EventsUser.objects.get_or_create(
            user=user,
            events=event,
            defaults={'user_rating': rating}
        )

        # If the object was not created, that means it already existed and we just update the rating
        if not created:
            event_user.user_rating = rating
            event_user.save()

        return Response({'message': 'Received'}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Events.DoesNotExist:
        return Response({'message': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)



