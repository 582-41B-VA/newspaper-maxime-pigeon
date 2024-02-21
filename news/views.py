from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from news.models import Article, Comment
from django.urls import reverse


def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "news/index.html", context)


def article(request, id):
    current_article = get_object_or_404(Article, pk=id)
    related_articles = Article.objects.filter(author=current_article.author)
    related_articles = related_articles.exclude(pk=id)
    comments = Comment.objects.filter(article=current_article)
    context = {
        "id": current_article.id,
        "title": current_article.title,
        "author": current_article.author,
        "related_articles": related_articles,
        "comments": comments,
    }
    return render(request, "news/article.html", context)


def comment(request, id):
    current_article = get_object_or_404(Article, pk=id)
    new_comment = Comment(
        name=request.POST["name"],
        age=request.POST["age"],
        comment_text=request.POST["comment_text"],
        article=current_article,
    )
    new_comment.save()
    article_url = reverse("article", args=[id])
    return HttpResponseRedirect(article_url)
