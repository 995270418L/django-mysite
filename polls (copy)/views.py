from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from .models import Question,Choice

# Create your views here.
# 首页
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
            'latest_question_list' : latest_question_list
            }
    return render(request,'polls/index.html',context)

# 问题详情页
def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

# 结果页面 votes
def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

# vote页面
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question' : question,
            'error_message': "You didn't select a choice.",
            })
    else:
        select_choice.vote += 1 
        select_choice.save()

        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
