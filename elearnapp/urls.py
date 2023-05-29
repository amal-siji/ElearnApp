from django.urls import path
from . import views
urlpatterns = [

    # main page
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('gallery/', views.gallery, name='gallery'),

    # teacher
    path('teacher/register/', views.tr_registration, name='tr_registration'),
    path('teacher/login/', views.tr_login, name='tr_login'),
    path('tr_home/', views.home, name='tr_home'),
    path('tr_profile/', views.tr_profile, name='tr_profile'),
    path('tr_profile_edit/<int:id>', views.tr_profile_edit, name='tr_profile_edit'),
    path('tr_changepassword/', views.password_change, name='tr_changepassword'),
    path('tr_show_st', views.tr_show_st, name='tr_show_st'),
    path('exam', views.exam_add, name='add_exam'),
    path('showexam', views.exam_notify, name='examnotify'),

    # student
    path('student/register', views.st_registration, name='st_registration'),
    path('student/login', views.st_login, name='st_login'),
    path('st_home/', views.st_home, name='st_home'),
    path('st_profile/', views.st_profile, name='st_profile'),
    path('st_changepassword/', views.st_password_change, name='st_changepassword'),
    path('st_edit/<int:id>', views.st_profile_edit, name='st_edit'),

    # admin
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_show_st', views.admin_show_st, name='admin_show_st'),
    path('admin_show_tr/', views.admin_show_tr, name='admin_show_teacher'),
    path('admin_show_exam', views.exam, name='admin_exams'),
    path('admin_show_contactepeoples',
         views.admin_show_contacted_peoples, name='admin_show_peoples'),
    path('ad_changepassword/', views.ad_password_change, name='ad_changepassword'),
    path('delete_tr/<int:id>', views.tr_delete, name='tr_delete'),
    path('delete_st/<int:id>', views.st_delete, name='st_delete'),
    path('delete_contacted_people/<int:id>',
         views.ad_delete_contact, name='ad_delete_contact'),

    # Messages
    path('trsendmsgs/', views.tr_send_messages, name='trsendmsgs'),
    path('trshowmsgs/', views.tr_show_messages, name='trshowmsgs'),
    path('stsendmsgs/', views.st_send_messages, name='stsendmsgs'),
    path('stshowmsgs/', views.st_show_messages, name='stshowmsgs'),
    path('adsendmsgs/', views.ad_send_messages, name='adsendmsgs'),
    path('adshowmsgs/', views.ad_show_messages, name='adshowmsgs'),

]
