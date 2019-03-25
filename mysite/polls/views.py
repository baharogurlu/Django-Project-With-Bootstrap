

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader, RequestContext
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required

 #Create your views here.

@login_required(login_url='login/')
def  index(request):
    latest_question = Question.objects.order_by('-pub_date')[:5] #pubdate e göre sıralı olanları 5 tanesini aldı,- işareti en son eklenenden başlayarak sıralar
    context = RequestContext(request, {
        'latest_question': latest_question
    })

    context_dict = context.flatten()
    template= loader.get_template('polls/index.html')

    return HttpResponse(template.render(context_dict))

@login_required(login_url='login/')
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = RequestContext(request, {'question': question}).flatten()
    return render(request, 'polls/detail.html', context)

@login_required(login_url='login/')
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question, 'error_message': 'please select choice'})

@login_required(login_url='login/')
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

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/polls/1')
    return render(request, 'polls/login.html')



