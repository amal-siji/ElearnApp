from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Contact(models.Model):
    name = models.EmailField(max_length=255, null=True)
    email = models.CharField(max_length=10000)
    message = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.name

class TeacherProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True, upload_to="tcrimages/", blank=True)

    def __unicode__(self):
        return self.user
    
class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to="tcrimages/", blank=True)

    def __unicode__(self):
        return self.username

class student_exam(models.Model):
    subject = models.CharField(max_length=255)
    Portion = models.CharField(max_length=255, null=True)
    Datetime = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __unicode__(self):
        return self.subject

class message_app(models.Model):
    sender = models.CharField(max_length=255, null=True)
    reciever = models.CharField(max_length=255, null=True)
    message_content = models.TextField(max_length=255, null=True)
