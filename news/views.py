from django.shortcuts import render

from django.http import HttpResponse
from news.models import Article


def index(request):
    articles = Article.objects.all()
    res = HttpResponse()
    for a in articles:
        res.write(a.title + "\n")
    return res


def article(request, id):
    current_article = Article.objects.get(pk=id)
    res = HttpResponse()
    res.write(f"Title: {current_article.title}\n")
    res.write(
        f"Author: {current_article.author.first_name} {current_article.author.last_name}\n"
    )
    res.write(f"Text: {current_article.article_text}\n")

    related_articles = Article.objects.filter(author=current_article.author).exclude(
        pk=id
    )
    res.write("\nRelated articles:\n")
    for a in related_articles:
        res.write(a.title + "\n")

    return HttpResponse(res)
