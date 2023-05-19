from django.db import models

# Create your models here.

class University(models.Model):
    uni_name = models.CharField(max_length=255)


class Organizers(models.Model):
    org_first_name = models.CharField(max_length=255)
    org_last_name = models.CharField(max_length=255)
    org_img = models.SlugField(null=True)


class Categories(models.Model):
    categ_name = models.CharField(max_length=255)


class Postitions(models.Model):
    pos_name = models.CharField(max_length=255)
    pos_description = models.CharField(max_length=255)
    pos_img = models.SlugField(null=True)


class EventsCategories(models.Model):
    events = models.ForeignKey('Events', on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventscategories'
        unique_together = (('events', 'categories'),)


class EventsPositions(models.Model):
    events = models.ForeignKey('Events', on_delete=models.CASCADE)
    postitions = models.ForeignKey(Postitions, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventspostitions'
        unique_together = (('events', 'postitions'),)


class EventsOrganizers(models.Model):
    events = models.ForeignKey('Events', on_delete=models.CASCADE)
    organizers = models.ForeignKey(Organizers, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'eventsorganizers'
        unique_together = (('events', 'organizers'),)


class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    capacity = models.IntegerField()
    price = models.IntegerField()
    rating = models.IntegerField()
    img = models.SlugField()
    categories = models.ManyToManyField(Categories, through=EventsCategories, null=True)
    positions = models.ManyToManyField(Postitions, through=EventsPositions, null=True)
    organizers = models.ManyToManyField(Organizers, through=EventsOrganizers, null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE, null=True)
    password = models.CharField(max_length=255, default='-')
    email = models.EmailField()
    phone = models.CharField(max_length=255)


class Volunteer(models.Model):
    position = models.CharField(max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

