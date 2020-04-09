# Create your views here.

from .models import Question
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

def get_list_of_questions(request):
    question_list=Question.objects.all()
    if(request.GET.get('sort_by')=='asc'):
        question_list=Question.objects.all().order_by('text')
    elif(request.GET.get('sort_by')=='desc'):
        question_list=Question.objects.all().order_by('-text')
    return render(request, 'get_list_of_questions.html', {'question_list': question_list})
def create_question(request):
    if(request.method=='GET'):
        return render(request, 'create_question_form.html')
    elif(request.method=='POST'):
        if(request.POST.get('question') and request.POST.get('answer')):
            question=Question(text=request.POST.get('question'),answer=request.POST.get('answer'))
            question.save()
            return render(request,'create_question_success.html')
        else:
            return render(request,'create_question_failure.html')
            
def get_question(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request, 'each_question_form.html',{'question':question})
    
def update_question(request,question_id):
    print(request.method)
    if(request.method=='GET'):
        question=get_object_or_404(Question,pk=question_id)
        return render(request, 'each_question_form.html',{'question':question})
    elif(request.method=='POST'):
        if(request.POST.get('question') and request.POST.get('answer')):
            question=Question.objects.get(id=question_id)
            question.text=request.POST.get('question')
            question.answer=request.POST.get('answer')
            question.save()
            return render(request,'update_question_success.html')
        else:
            return render(request,'update_question_failure.html')
        
def delete_question(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return render(request,'delete_question_failure.html')
    question.delete()
    return render(request,'delete_question_success.html')