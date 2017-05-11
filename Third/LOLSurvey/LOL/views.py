from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'LOL/index.html'

    def get_queryset(self):
        return

class DetailView(generic.ListView):
    """
    Return the last five published question(not include those set to be published in the future)
    :return:
    """
    template_name = 'LOL/questionnaire.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()

class ResultView(generic.DetailView):
    model = Question
    template_name = 'LOL/result.html'

    def get_queryset(self):
        return


def result(request, question_id):
    qeustion = get_object_or_404(Question, pk=question_id)
