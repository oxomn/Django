from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    (... 생략 ...)


def detail(request, question_id):
    (... 생략 ...)