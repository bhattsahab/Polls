from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from Letspoll.models import Question, Vote
from django.core.urlresolvers import reverse


def index(request):
  latest_question_list = Question.objects.order_by('-date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'Letspoll/index.html', context)


def detail(request, querry_id):
  question = Question.objects.get(pk=querry_id)
  return render(request, 'Letspoll/detail.html', {'question': question})

def results(request, querry_id):
  question = get_object_or_404(Question, pk=querry_id)
  return render(request, 'Letspoll/results.html', {'question':question})

def casted_vote(request, querry_id):
  p= get_object_or_404(Question, pk=querry_id)
  try:
     selected_choice = p.vote_set.get(pk=request.POST['myvote'])
  except (KeyError, Vote.DoesNotExist):
     return render(request, 'Letspoll/detail.html' , {
         'question': p,
         'error_message': "You didn't select a choice.",
     })
  else:
     selected_choice.votes += 1
     selected_choice.save()
     return HttpResponseRedirect(reverse('Letspoll:results', args=(p.id, )))

