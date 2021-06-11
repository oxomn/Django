from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import CommentForm
from ..models import Question, Answer, Comment


@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    (... 생략 ...)


@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    (... 생략 ...)


@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    (... 생략 ...)


@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    (... 생략 ...)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    (... 생략 ...)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    (... 생략 ...)