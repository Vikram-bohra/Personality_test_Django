from django.shortcuts import render,redirect,HttpResponse
from .models import Questions,Student
from .form import stu_form
global c
global l,stu_name,stu_marks
l = []
name = ""
c = 1
def question_view(request):
    global c
    global l
    try:
        data = Questions.objects.get(id = c)
    except:
        c = 1
        return redirect("stu_name")
    return render(request,"dashboard.html",{'i' : data})

def marks_post(request,marks):
    global c
    global l
    l.append(marks)
    c = c+1
    return redirect('questions')

def student_name(request):
    global stu_name,l,stu_marks
    stu_name = name
    stu_marks = sum(l)
    form = stu_form(request.POST)
    if form.is_valid():
        stu_name = form.cleaned_data['name']
        Student.objects.create(name=stu_name, mark=sum(l))
        l = []
        return redirect('final_page')
        # Student.objects.create(name = stu_name,mark = sum(l))
    else:
        form = stu_form()
    return render(request,"first_page.html",{'form':form})

def final_page(request):
    global stu_name,stu_marks
    if stu_marks < 50:
        per =['The Guider', '''
    You are accepted everywhere
    People loves you
    because you are good listner,communicator and have a good sense of humor.
    You have an intutive sense of the emotions of others,and often act as an emotional barometer for the people around them.''',
    '''The best jobs for you
    Market research analyst
    public relations specialist
    teacher
    social worker
    therapist''']
    if stu_marks >= 50 and stu_marks < 100:
        per = ['The Artist','''
    You are happy to be who you are.
    You live in a colorful world inspired by connections with people and ideas.
    The biggest challenge for you is planning for the future.
    finding constructive ideals to base their goals on and working out goals is the hardest things to do.''',
    '''The Jobs for you are
    Artist,Graphic Designer, Arhitect, Fashion designer, Photographer, Actor/Actress, Writer,Editor.''']

    if stu_marks >= 100 and stu_marks < 150:
        per =['The Leader', '''
    You are special,you can be whoever you like.
    People in this type embody the gifts of charisma and confidence.''',
    '''The Jobs for you are Judge, Lawyer, Enterpreneur, project manager, accountant, financial advisor.''']

    if stu_marks >= 150:
        per =['The Scientist', '''
    You are a genius thats super hard to find.
    You enjoys theoretical and abstact concepts,dislikes confusion,disorientaion and inefficiency.
    You are more focused on the future than on the present.''',
    '''The Jobs for you are Scientist, doctor, pilot, austronuat, computer programmer''']

    return render(request,"final.html",{'name':stu_name.capitalize,'marks':stu_marks,'personality':per})


