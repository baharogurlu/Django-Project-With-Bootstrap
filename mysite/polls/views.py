

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader, RequestContext
from django.urls import reverse

 #Create your views here.

def  index(request):
    latest_question = Question.objects.order_by('-pub_date')[:5] #pubdate e göre sıralı olanları 5 tanesini aldı,- işareti en son eklenenden başlayarak sıralar
    context = RequestContext(request, {
        'latest_question': latest_question
    })

    context_dict = context.flatten()
    template= loader.get_template('polls/index.html')

    return HttpResponse(template.render(context_dict))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = RequestContext(request, {'question': question}).flatten()
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question, 'error_message': 'please select choice'})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except:
        print('Except e girdi-----')
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'please select choice'})
    else:
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

