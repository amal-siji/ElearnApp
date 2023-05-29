from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth.forms import SetPasswordForm

# Teacher
coursechoice = [
    ('select choice', 'selectChoice'),
    ('Python Django', 'Python Django'),
    ('c#', 'c#'),
    ('C++', 'C++'),
    ('UI/UX', 'UI/UX'),
    ('React', 'React'),]


class TeacherRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    subject = forms.CharField(
        label="select Your Subject", widget=forms.Select(choices=coursechoice))
    image = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'subject',
            'image',
            'username',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super(TeacherRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(TeacherRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            TeacherProfile.objects.create(
                image=self.cleaned_data["image"], subject=self.cleaned_data["subject"], user=user)
        return user


class TeacherLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User()
        fields = ['password1', 'password2']


class tr_edit_form(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(
        label="select Your Subject", widget=forms.Select(choices=coursechoice))
    image = forms.ImageField()
 
    class Meta:
        model = TeacherProfile
        fields = "__all__"
        exclude = ('user', 'subject', 'image', 'subject')

    def save(self, commit=True):
        user = super(tr_edit_form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            let = TeacherProfile.objects.get(user_id=user.id)
            let.image = self.cleaned_data["image"]
            let.subject = self.cleaned_data["subject"],
            let.user = user
            let.save()
        return user

# student


class StudentLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


coursechoice = [
    ('SelectChoice', 'SelectChoice'),
    ('Python Django', 'Python Django'),
    ('c#', 'c#'),
    ('C++', 'C++'),
    ('UI/UX', 'UI/UX'),
    ('React', 'React'),
]


class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    skills = forms.CharField()
    address = forms.CharField(max_length=100)
    course = forms.CharField(label="select Your Course",
                             widget=forms.Select(choices=coursechoice))
    image = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'skills',
            'address',
            'course',
            'image',
            'username',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super(StudentRegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(StudentRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            StudentProfile.objects.create(
                image=self.cleaned_data["image"], skills=self.cleaned_data["skills"], address=self.cleaned_data["address"], course=self.cleaned_data["course"], user=user)
        return user


class StPasswordForm(SetPasswordForm):
    class Meta:
        model = User()
        fields = ['password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].help_text = None


class st_edit_form(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=255)
    skills = forms.CharField(max_length=255)
    course = forms.CharField(max_length=255)

    class Meta:
        model = StudentProfile
        fields = "__all__"
        exclude = ('user', 'subject', 'image', 'skills',
                   'address', 'course', 'course')


class Examform(forms.ModelForm):
    class Meta:
        model = student_exam
        fields = "__all__"


class Admin_loginform(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].help_text = None


class MessageForm(forms.ModelForm):
    reciever = forms.CharField(max_length=255)
    message_content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = message_app
        fields = ['reciever', 'message_content']
