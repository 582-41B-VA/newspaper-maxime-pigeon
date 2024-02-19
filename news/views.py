from django.shortcuts import get_object_or_404 ,render
from news.models import Article


def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "news/index.html", context)


def article(request, id):
    current_article = get_object_or_404(Article, pk=id)
    related_articles = Article.objects.filter(author=current_article.author).exclude(
        pk=id
    )
    context = {
        "title": current_article.title,
        "author": current_article.author,
        "related_articles": related_articles,
    }
    return render(request, "news/article.html", context)
