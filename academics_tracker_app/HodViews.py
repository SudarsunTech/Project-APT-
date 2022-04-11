from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Sum
import json
from academics_tracker_app.models import CustomUser, exams, Courses, Subjects, SessionYearModel, Summary, Report
from .forms import AddStudentForm, EditStudentForm

def admin_home(request):
    subject_count = Subjects.objects.all().count()
    course_count = Courses.objects.all().count()
    exam_count = exams.objects.all().count()
    course_all = Courses.objects.all()
    course_name_list = []
    subject_count_list = []
    for course in course_all:
        subjects = Subjects.objects.filter(course_id=course.id).count()
        course_name_list.append(course.course_name)
        subject_count_list.append(subjects)
    subject_all = Subjects.objects.all()
    subject_list = []
    for subject in subject_all:
        course = Courses.objects.get(id=subject.course_id.id)
        subject_list.append(subject.subject_name)
    
    # For Exams
    exam_name_list=[]
    Exams = exams.objects.all()
    for exam in Exams:
        subject_ids = Subjects.objects.filter(exam_id=exam.id)
        exam_name_list.append(exam.exam_name)

    context={
        "subject_count": subject_count,
        "course_count": course_count,
        "exam_count": exam_count,
        "course_name_list": course_name_list,
        "subject_count_list": subject_count_list,
        "subject_list": subject_list,
        "exam_name_list": exam_name_list
    }
    return render(request, "hod_template/home_content.html", context)

def add_exam(request):
    return render(request, "hod_template/add_exam_template.html")

def add_exam_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_exam')
    else:
        exam_name = request.POST.get('exam_name')
        total_score = request.POST.get('total_score')
        target_score = request.POST.get('target_score')
        exams_model = exams(exam_name=exam_name, total_score=total_score,target_score = target_score)
        exams_model.save()
        messages.success(request, "Exam Added Successfully!")
        return redirect('add_exam')

def manage_exam(request):
    Exams = exams.objects.all()
    context = {
        "exams": Exams
    }
    return render(request, "hod_template/manage_exam_template.html", context)

def edit_exam(request, exam_id):
    exam = exams.objects.get(id=exam_id)

    context = {
        "exam": exam,
        "id": exam_id
    }
    return render(request, "hod_template/edit_exam_template.html", context)

def edit_exam_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        exam_id=request.POST.get('exam_id')
        exam_name = request.POST.get('exam_name')
        total_score = request.POST.get('total_score')
        target_score = request.POST.get('target_score')
        try:
            exam_model = exams.objects.get(id=exam_id)
            exam_model.exam_name = exam_name
            exam_model.total_score = total_score
            exam_model.target_score = target_score
            exam_model.save()
            messages.success(request, "Exam Updated Successfully.")
            return redirect('/edit_exam/'+exam_id)
        except:
            messages.error(request, "Failed to Update Exam.")
            return redirect('/edit_exam/'+exam_id)

def delete_exam(request, exam_id):
    exam = exams.objects.get(id=exam_id)
    try:
        exam.delete()
        messages.success(request, "Exam Deleted Successfully.")
        return redirect('manage_exam')
    except:
        messages.error(request, "Failed to Delete Exam.")
        return redirect('manage_exam')

def add_course(request):
    return render(request, "hod_template/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_course')
    else:
        course = request.POST.get('course')
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('add_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('add_course')

def manage_course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'hod_template/manage_course_template.html', context)

def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    context = {
        "course": course,
        "id": course_id
    }
    return render(request, 'hod_template/edit_course_template.html', context)

def edit_course_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course')

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()
            messages.success(request, "Course Updated Successfully.")
            return redirect('/edit_course/'+course_id)

        except:
            messages.error(request, "Failed to Update Course.")
            return redirect('/edit_course/'+course_id)

def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    try:
        course.delete()
        messages.success(request, "Course Deleted Successfully.")
        return redirect('manage_course')
    except:
        messages.error(request, "Failed to Delete Course.")
        return redirect('manage_course')

def manage_session(request):
    session_years = SessionYearModel.objects.all()
    context = {
        "session_years": session_years
    }
    return render(request, "hod_template/manage_session_template.html", context)

def add_session(request):
    return render(request, "hod_template/add_session_template.html")

def add_session_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_course')
    else:
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')
        try:
            sessionyear = SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request, "Session Year added Successfully!")
            return redirect("add_session")
        except:
            messages.error(request, "Failed to Add Session Year")
            return redirect("add_session")

def edit_session(request, session_id):
    session_year = SessionYearModel.objects.get(id=session_id)
    context = {
        "session_year": session_year
    }
    return render(request, "hod_template/edit_session_template.html", context)

def edit_session_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('manage_session')
    else:
        session_id = request.POST.get('session_id')
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        try:
            session_year = SessionYearModel.objects.get(id=session_id)
            session_year.session_start_year = session_start_year
            session_year.session_end_year = session_end_year
            session_year.save()
            messages.success(request, "Session Year Updated Successfully.")
            return redirect('/edit_session/'+session_id)
        except:
            messages.error(request, "Failed to Update Session Year.")
            return redirect('/edit_session/'+session_id)

def delete_session(request, session_id):
    session = SessionYearModel.objects.get(id=session_id)
    try:
        session.delete()
        messages.success(request, "Session Deleted Successfully.")
        return redirect('manage_session')
    except:
        messages.error(request, "Failed to Delete Session.")
        return redirect('manage_session')

def add_subject(request):
    courses = Courses.objects.all()
    Exams = exams.objects.all()
    context = {
        "courses": courses,
        "exams": Exams
    }
    return render(request, 'hod_template/add_subject_template.html', context)

def add_subject_save(request):
    if request.method != "POST":
        messages.error(request, "Method Not Allowed!")
        return redirect('add_subject')
    else:
        course_id = request.POST.get('course')
        course = Courses.objects.get(id=course_id)
        exam_id = request.POST.get('exam')
        exam = exams.objects.get(id=exam_id)
        subject_name = request.POST.get('subject')
        marks_scored = request.POST.get('marks')
        try:
            subject = Subjects(subject_name=subject_name, course_id=course, exam_id=exam,marks_scored=marks_scored)
            subject.save()
            messages.success(request, "Subject Added Successfully!")
            return redirect('add_subject')
        except:
            messages.error(request, "Failed to Add Subject")
            return redirect("add_subject")

def manage_subject(request):
    subjects = Subjects.objects.all()
    context = {
        "subjects": subjects
    }
    return render(request, 'hod_template/manage_subject_template.html', context)

def edit_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    courses = Courses.objects.all()
    Exams = exams.objects.all()
    context = {
        "subject": subject,
        "courses": courses,
        "exams": Exams,
        "id": subject_id,
    }
    return render(request, 'hod_template/edit_subject_template.html', context)

def edit_subject_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method.")
    else:
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject')
        course_id = request.POST.get('course')
        exam_id = request.POST.get('exam')
        marks_scored=request.POST.get('marks')        
        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name
            subject.marks_scored = marks_scored
            course = Courses.objects.get(id=course_id)
            subject.course_id = course
            exam = exams.objects.get(id=exam_id)
            subject.exam_id = exam
            subject.save()
            messages.success(request, "Subject Updated Successfully.")
            # return redirect('/edit_subject/'+subject_id)
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))
        except:
            messages.error(request, "Failed to Update Subject.")
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))
            # return redirect('/edit_subject/'+subject_id)

def delete_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    try:
        subject.delete()
        messages.success(request, "Subject Deleted Successfully.")
        return redirect('manage_subject')
    except:
        messages.error(request, "Failed to Delete Subject.")
        return redirect('manage_subject')

def show_summary(request):
    Exams = exams.objects.all()
    courses = Courses.objects.all()
    subjects = Subjects.objects.all()
    summary = Summary.objects.all()
    report=Report.objects.all()
    context = {
        "exams": Exams,
        "courses": courses,
        "subjects": subjects,
        "summary": summary,
        "report": report
    }
    return render(request, 'hod_template/summary_template.html', context)

def summary_content(request):
    if request.method != "POST":
        return redirect('show_summary')
    else:
        Summary.objects.all().delete()
        Report.objects.all().delete()
        course_id = request.POST.get('course')
        course = Courses.objects.get(id=course_id)
        subject_id = request.POST.get('subject')
        subject = Subjects.objects.get(id=subject_id)

        total = exams.objects.aggregate(Sum('total_score'))
        target = exams.objects.aggregate(Sum('target_score'))
        exp=(list(target.values())[0])/(list(total.values())[0])*100
        scored = Subjects.objects.filter(subject_name=subject.subject_name).aggregate(marks_scored=Sum('marks_scored'))
        obt=(list(scored.values())[0])/(list(total.values())[0])*100
        diff=obt-exp
        if diff<0:
            out='Improvement needed'
        elif diff==0:
            out='Target Achieved'
        else:
            out='Did Better'
                
        try:
            summary = Summary(course_id=course, subject_id=subject)
            summary.save()
            report = Report(expected_percent=exp,scored_percent=obt,difference=diff,outcome=out)
            report.save()
            return redirect('show_report')
        
        except:
            messages.error(request, "Failed to Generate Report")
            return redirect("show_summary")

def show_report(request):
    Exams = exams.objects.all()
    courses = Courses.objects.all()
    subjects = Subjects.objects.all()
    summary = Summary.objects.all()
    report=Report.objects.all()
    context = {
        "exams": Exams,
        "courses": courses,
        "subjects": subjects,
        "summary": summary,
        "report": report
    }
    return render(request, 'hod_template/report.html',context)
    
@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context={
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)

def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')
