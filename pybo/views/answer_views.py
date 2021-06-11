from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:login')
def answer_create(request, question_id):
    (... 생략 ...)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    (... 생략 ...)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    (... 생략 ...)