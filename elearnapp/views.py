from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from . forms import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from .forms import SetPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# common


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    if request.method == "POST":
        usname = request.POST.get('usname')
        print(usname)
        email = request.POST.get('email')
        print(email)
        message = request.POST.get('message')
        contact_list = Contact.objects.create(
            name=usname, email=email, message=message)
        contact_list.save()
        print('form saved')
        messages.success(request, 'Message sended')

    return render(request, 'contactus.html')


def gallery(request):
    return render(request, 'gallery.html')

# teachers


def tr_registration(request):
    form = TeacherRegisterForm()
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('form saved')
            messages.info(request, "Registration sucessfull.")
            return redirect('tr_login')
        else:
            form = TeacherRegisterForm()
            print("form not saved")
            messages.error(request, "Registration unsucessfull.")
    context = {'form': form}
    return render(request, 'teachers/tr_registration.html', context)


def tr_login(request):
    form = TeacherLoginForm()
    if request.method == 'POST':
        form = TeacherLoginForm(data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if form.is_valid():
            if user is not None:
                auth_login(request, user)
                return redirect('tr_home')
            else:
                print("user not found")
        else:
            form = TeacherLoginForm()
    context = {'form': form}
    return render(request, 'teachers/tr_login.html', context)


@login_required
def logout(request):
    logout(request.user)
    return redirect('index')


@login_required
def home(request):
    return render(request, 'teachers/tr_home.html')


@login_required
def tr_profile(request):
    profile = TeacherProfile.objects.get(user_id=request.user.id)
    context = {'t_profile': profile}
    return render(request, 'teachers/tr_profile.html', context)


@login_required
def tr_profile_edit(request, id):
    Edituser = User.objects.prefetch_related(
        'teacherprofile_set').filter(id=id).first()
    form = tr_edit_form(instance=Edituser)
    if request.method == "POST":
        form = tr_edit_form(request.POST, request.FILES, instance=Edituser)
        print("form taken")
        if form.is_valid():
            print("valid")
            form.save()
            print("edited")
            return redirect('tr_profile')
            messages.info(request, " edited")
        else:
            print("not edited")
    context = {'form': form, 'id': id}
    return render(request, "teachers/tr_edit.html", context)


@login_required
def tr_show_st(request):
    show_students = StudentProfile.objects.all()
    print(show_students)
    context = {
        'show_students': show_students}
    return render(request, "teachers/tr_show_st.html", context)


@login_required
def password_change(request):
    form = SetPasswordForm(request.user)
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            print("password changed")
            return redirect("tr_login")
        else:
            form = SetPasswordForm(request.user)

    context = {'form': form}
    return render(request,  'teachers/tr_changepassword.html', context)


@login_required
def exam_add(request):
    addform = Examform()
    if request.method == 'POST':
        addform = Examform(request.POST)
        print(addform)
        if addform.is_valid():
            addform.save()
            print("Exam added")
            messages.info(request, "exam added")
            return redirect("tr_home",)
        else:
            addform = Examform()
            print("not added")
    context = {
        'addform': addform}
    return render(request, 'teachers/exams.html', context)

# students


def st_registration(request):
    form = StudentRegisterForm()
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('form saved')
            return redirect('st_login')
        else:
            form = StudentRegisterForm()
            messages.error(request, 'registration unsuccessfull')
    context = {'form': form}
    return render(request, 'student/st_registration.html', context)


def st_login(request):
    form = StudentLoginForm()
    if request.method == 'POST':
        form = StudentLoginForm(data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            if user is not None:
                auth_login(request, user)
                return redirect('st_home')
            else:
                print("user not found")
        else:
            form = StudentLoginForm()
    context = {'form': form}
    return render(request, 'student/st_login.html', context)


@login_required
def logout(request):
    logout(request.user)
    return redirect('index')


@login_required
def st_home(request):
    return render(request, "student/st_home.html")


@login_required
def st_profile(request):
    print(request.user.id)
    st_profile = StudentProfile.objects.get(user_id=request.user.id)
    context = {'profile': st_profile}
    return render(request, "student/st_profile.html", context)


@login_required
def st_profile_edit(request, id):
    Edituser = User.objects.prefetch_related(
        'studentprofile_set').filter(id=id).first()
    form = st_edit_form(instance=Edituser)
    if request.method == "POST":
        form = st_edit_form(data=request.POST, instance=Edituser)
        print(id)
        if form.is_valid():
            form.save()
            print("edited")
            messages.info(request, " edited")
            return redirect('st_profile')
        else:
            print("not edited")
    context = {'form': form, 'id': id}
    return render(request, "student/st_edit.html", context)


@login_required
def st_password_change(request):
    form = StPasswordForm(request.user)
    if request.method == 'POST':
        form = StPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            print("password changed")
            messages.success(request, 'Password Changed')
            return redirect("st_login")
        else:
            form = StPasswordForm(request.user)

    context = {'form': form}
    return render(request, "student/st_changepassword.html", context)


@login_required
def st_edit(request):
    Editprofile = StudentProfile.objects.get(user_id=id).prefetch_related(User)
    form = st_edit_form(instance=Editprofile)
    if request.method == "POST":
        form = st_edit_form(data=request.POST, instance=Editprofile)

        if form.is_valid():
            form.save()
            print("edited")
            messages.info(request, " edited")
            return redirect('st_profile')
        else:
            print("not edited")
    context = {'form': form, 'id': id}
    return render(request, "student/st_edit.html", context)


@login_required
def st_message(request):
    return render(request, "student/st_message.html")


@login_required
def exam_notify(request):
    notification = student_exam.objects.all()
    print(notification)
    context = {'notification': notification}
    return render(request, 'student/studentexam.html', context)

# Admin


def admin_login(request):
    form = Admin_loginform()
    if request.method == 'POST':
        form = Admin_loginform(data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            if user.is_superuser:
                auth_login(request, user)
                return redirect('admin_home')
            else:
                print("user not found")
                return redirect('admin_login')
        else:
            form = Admin_loginform()
    context = {'form': form}
    return render(request, 'admin/admin_login.html', context)


@login_required
def admin_home(request):
    return render(request, 'admin/admin_home.html')


@login_required
def admin_show_st(request):
    show_students = StudentProfile.objects.all()
    print(show_students)
    context = {
        'show_students': show_students}
    return render(request, "admin/admin_show_st.html", context)


@login_required
def admin_show_tr(request):
    show_teachers = TeacherProfile.objects.all()
    print(show_teachers)
    context = {
        'show_teachers': show_teachers}
    return render(request, "admin/admin_show_tr.html", context)


@login_required
def ad_password_change(request):
    form = StPasswordForm(request.user)
    if request.method == 'POST':
        form = StPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            print("password changed")
            return redirect("admin_login")
        else:
            form = StPasswordForm()

    context = {'form': form}
    return render(request, 'admin/ad_changepassword.html', context)


@login_required
def tr_delete(request, id):
    delete_tr = User.objects.get(id=id)
    delete_tr.delete()
    messages.error(request, "deleted")
    return redirect('admin_show_teacher')


@login_required
def st_delete(request, id):
    delete_student = StudentProfile.objects.get(id=id)
    delete_student.delete()
    messages.error(request, "deleted")
    return redirect('admin_show_st')


@login_required
def ad_delete_contact(request, id):
    delete_contact = Contact.objects.get(id=id)
    delete_contact.delete()
    messages.error(request, "deleted")
    return redirect('admin_show_peoples')


@login_required
def exam(request):
    notification = student_exam.objects.all()
    print(notification)
    context = {'notification': notification}
    return render(request, 'admin/admin_exams.html', context)


@login_required
def admin_show_contacted_peoples(request):
    contact = Contact.objects.all()
    print(contact)
    context = {"contactedpeople": contact}
    return render(request, "admin/admin_contactedpeoples.html", context)


@login_required
def send_messages(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            your_object = form.save(commit=False)
            your_object.sender = request.user.username
            your_object.save()
            return redirect("tr_home")
        else:
            print("check the data")
    context = {'form': form}
    return render(request, 'sendmessages.html', context)


@login_required
def show_messages(request):
    my_msgs = message_app.objects.filter(reciever=request.user.username)
    context = {'my_msgs': my_msgs}
    return render(request, 'showmessages.html', context)


@login_required
def st_show_messages(request):
    my_msgs = message_app.objects.filter(reciever=request.user.username)
    context = {'my_msgs': my_msgs}
    return render(request, 'student/st_show_message.html', context)


@login_required
def tr_show_messages(request):
    my_msgs = message_app.objects.filter(reciever=request.user.username)
    context = {'my_msgs': my_msgs}
    return render(request, 'teachers/tr_showmessages.html', context)


@login_required
def ad_show_messages(request):
    my_msgs = message_app.objects.filter(reciever=request.user.username)
    context = {'my_msgs': my_msgs}
    return render(request, 'admin/ad_showmessages.html', context)


@login_required
def tr_send_messages(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            your_object = form.save(commit=False)
            your_object.sender = request.user.username
            your_object.save()
            return redirect("tr_home")
        else:
            print("check the data")
    context = {'form': form}
    return render(request, 'teachers/tr_sendmessage.html', context)


@login_required
def ad_send_messages(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            your_object = form.save(commit=False)
            your_object.sender = request.user.username
            your_object.save()
            return redirect("tr_home")
        else:
            print("check the data")
    context = {'form': form}
    return render(request, 'admin/ad_sendmessage.html', context)


@login_required
def st_send_messages(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            your_object = form.save(commit=False)
            your_object.sender = request.user.username
            your_object.save()
            return redirect("st_home")
        else:
            print("check the data")
    context = {'form': form}
    return render(request, 'student/st_sendmessages.html', context)
