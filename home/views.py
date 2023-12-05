import contextlib
from django.shortcuts import render, redirect
from . models import News, NewsThumbnill, Element, NewsCategory
from django.db.models import Q
# Create your views here.


def get_news(object, length):
    with contextlib.suppress(Exception):
        object = object[:length]
    return object


def home(request):
    news_thumbnills = NewsThumbnill.objects.all()
    all_news = News.objects.all()
    breaking_news = News.objects.filter(is_breaking=True)

    news_thumbnills = get_news(news_thumbnills, 15)
    top_news = get_news(all_news, 6)
    breaking_news = get_news(breaking_news, 6)
    params = {
        'home': True,
        'top_news': top_news,
        'breaking_news': breaking_news,
        'news_thumbnills': news_thumbnills,
        'all_news': all_news
    }
    return render(request, 'home/index.html', params)


def news(request, slug):
    try:
        news = News.objects.get(slug=slug)
        all_news = News.objects.all()
        breaking_news = News.objects.filter(is_breaking=True)
        top_news = get_news(all_news, 6)
        breaking_news = get_news(breaking_news, 6)
        news_card = {'breaking': breaking_news, 'top': top_news}

        category = news.news_category.all()
        category = [i.category for i in category]
        hashtag = news.news_hashtag.all()
        hashtag = [i.hashtag for i in hashtag]

        elements = Element.objects.filter(news=news).order_by('order_no')

        params = {'news': news, 'news_cards': news_card,
                  'elements': elements, 'categories': category, 'hashtag': hashtag}
    except Exception:
        return redirect('home')

    return render(request, 'home/news.html', params)


def search(request):
    search_query = request.GET.get('search')

    s1 = list(News.objects.filter(heading__contains=search_query))
    s2 = Element.objects.filter(text__contains=search_query)
    s3 = NewsCategory.objects.filter(category__text__contains=search_query)

    s2 = [i.news for i in s2 if i is not None]
    s3 = [i.news for i in s3 if i is not None]
    news = set(s1+s2+s3)
    return render(request, 'home/search.html', {'news': news, 'search_query': search_query})
