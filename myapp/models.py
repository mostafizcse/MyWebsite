from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class author(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture=models.FileField()
    details = models.TextField()
    def __str__(self):
        return self.name.username

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class article(models.Model):
    article_author = models.ForeignKey(author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


#class Teammember(models.Model):
#    article_author = models.ForeignKey(author, on_delete=models.CASCADE)
#    image = models.FileField()
#    title = models.CharField(max_length=200)
#    subtital = models.CharField(max_length=400)
#    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
#    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
#    category = models.ForeignKey(category, on_delete=models.CASCADE)
#    def __str__(self):
#        return self.title


class Logo(models.Model):
    image = models.FileField(blank=True)

class Team(models.Model):
    image = models.FileField(blank=True)
    tital = models.CharField(max_length=300)
    subtitl = models.CharField(max_length=300)

class TeamTital(models.Model):
    name = models.CharField(max_length=400)
    deciption = models.TextField()

class Reviewstitle(models.Model):
    name = models.CharField(max_length=400)
    deciption = models.TextField()

class Reviewlist(models.Model):
    name = models.CharField(max_length=200)
    deciption = models.TextField()

class slider(models.Model):
    sliderimage = models.FileField()
    tital = models.CharField(max_length=300)
    description = models.TextField()
    linktital = models.CharField(max_length=200)
    linkurl = models.URLField()


class Featuretitle(models.Model):
    title = models.CharField(max_length=400)
    details = models.TextField()

class Featurelist(models.Model):
    image = models.FileField(blank=True)
    tital = models.CharField(max_length=200)
    description = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    timestrimp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    posttitle = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=600)
    description = RichTextField()

    def __str__(self):
        return self.posttitle

class Events(models.Model):
    event = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        template = '{0.event} {0.location} {0.date}'
        return template.format(self)

class Requirments(models.Model):
    job_title = models.CharField(max_length=400)
    description = RichTextField()

    def __str__(self):
        return self.job_title


## example
class Example(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Create_menu(models.Model):
    Example =models.ForeignKey(Example, on_delete=models.CASCADE)
    m_name = models.CharField(max_length=300)
    m_title = models.CharField(max_length=200)
    description = RichTextField()


    def __str__(self):
        return self.m_name


class About_us(models.Model):
    description = models.TextField()


class Email_stor(models.Model):
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Address(models.Model):
    address = models.CharField(max_length=300)
    telephonnumber = models.CharField(max_length=300)
    email = models.EmailField()









