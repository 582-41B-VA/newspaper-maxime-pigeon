from django.http import HttpResponse
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    res = ""
    for q in latest_questions:
        res += q.question_text + "\n"
    return HttpResponse(res)


def detail(request, question_id):
    return HttpResponse(f"You're look at question {question_id}\n")


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}\n"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}\n")
