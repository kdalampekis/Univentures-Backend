from django.db import models


class University(models.Model):
    uni_name = models.CharField(max_length=255)


class Organization(models.Model):
    org_name = models.CharField(max_length=255)
    org_img = models.SlugField(null=True)


class Categories(models.Model):
    categ_name = models.CharField(max_length=255)
    categ_apr = models.CharField(max_length=255, default='-')
    categ_desc = models.TextField(default='-')


class EventsCategories(models.Model):
    events = models.ForeignKey('Events', on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventscategories'
        unique_together = (('events', 'categories'),)


class EventsOrganization(models.Model):
    events = models.ForeignKey('Events', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventsorganization'
        unique_together = (('events', 'organization'),)


class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    capacity = models.IntegerField()
    price = models.IntegerField()
    rating = models.IntegerField()
    img_src = models.SlugField(default='-')
    video_src = models.SlugField(default='https://www.youtube.com/embed/KtRHV9gH83U')
    categories = models.ManyToManyField(Categories, through=EventsCategories, null=True)
    organizers = models.ManyToManyField(Organization, through=EventsOrganization, null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Postitions(models.Model):
    pos_name = models.CharField(max_length=255)
    pos_description = models.CharField(max_length=255)
    pos_img = models.SlugField(null=True)
    event = models.ForeignKey(Events, null=True, on_delete=models.CASCADE)


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
    img_src = models.SlugField(default='-')
    location = models.CharField(max_length=255, default='-')
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)


class EventsUser(models.Model):
    user_rating = models.IntegerField(default=3)
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventsuser'
        unique_together = (('events', 'user'),)


class Volunteer(models.Model):
    PENDING = 'P'
    SUCCESS = 'S'
    FAIL = 'F'

    CHOICES = [
        (PENDING, 'Pending'),
        (SUCCESS, 'Success'),
        (FAIL, 'Fail')
    ]

    position = models.ForeignKey(Postitions, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default='-')
    status = models.CharField(max_length=1, choices=CHOICES, default=PENDING)


class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    event = models.ForeignKey(Events, on_delete=models.CASCADE)


class UsersCategories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'userpreferences'
        unique_together = (('user', 'categories'),)


class Features(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)


class Testimonials(models.Model):
    comment_title = models.TextField(default='-')
    comment = models.TextField(default='-')
    volunteer = models.ForeignKey(Volunteer, on_delete=models.PROTECT, null=True)

