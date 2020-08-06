from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from .forms import ArticleForm, UserMediaForm, CommentsForm
from .models import Article, UserProfile, Preferences, Comments


class HomePageView(View):
    """Home page"""

    def get(self, request):
        return render(request, "startup/home.html")


class AboutPageView(View):
    """About site page"""

    def get(self, request):
        return render(request, "startup/about.html")


class TeamPageView(View):
    """Team site page"""

    def get(self, request):
        creator = "grrame22"
        return render(request, "startup/team.html", {"creator": creator})


class ContactsPageView(View):
    """Contacts site page"""

    def get(self, request):
        return render(request, "startup/contacts.html")


class ArticlesViews(View):
    """List of Articles"""

    def get(self, request):
        articles = Article.objects.all()
        return render(request, "startup/articles_list.html",
                      {"articles_list": articles[::-1]})


def comments_article_view(request, slug):
    current_user = request.user

    comment = CommentsForm(request.POST or None)
    article = Article.objects.get(url=slug)

    if comment.is_valid():
        form_username = comment.cleaned_data.get("author")
        form_article = comment.cleaned_data.get("articles_name")

        if form_username == str(current_user):
            if form_article == str(article):
                comment.save()
                messages.success(request, "You have added a comment")
                return redirect("/article/" + slug)
            else:
                messages.error(request, "Please, enter the right article title")
                comment = CommentsForm()
        else:
            messages.error(request, "Please, enter your user name")
            comment = CommentsForm()

    return render(request, "startup/comment_create.html", {"comment": comment,
                                                           "article": article})


class ArticleDetailsView(View):
    """Details of article"""

    def get(self, request, slug):
        article = Article.objects.get(url=slug)

        all_comments = Comments.objects.filter(articles_name=slug)[::-1]
        comments_count = len(all_comments)
        return render(request, "startup/article_details.html",
                      {"article": article, "all_comments": all_comments,
                       "comments_count": comments_count})


class CategoriesView(View):
    """List of categories"""

    def get(self, request):
        category_list = Preferences.objects.all()

        return render(request, "startup/category_list.html",
                      {"category_list": category_list})


class ParticularCategoryView(View):
    """Particular category of article"""

    def get(self, request, id):
        category = Article.objects.filter(category=id)

        list_of_category_articles = len(category)
        category_id = id

        return render(request, "startup/category_article_list.html",
                      {"category": category, "category_id": category_id,
                       "list_of_category_articles": list_of_category_articles})


class UserMediaView(View):
    """User media"""

    def get(self, request, slug):
        user_media = UserProfile.objects.filter(user=slug)[::-1]
        user_media = user_media[0]

        return render(request, "startup/author_media.html",
                      {"user_media": user_media})


class AuthorDetailsView(View):
    """Details of article"""

    def get(self, request, slug):
        author = User.objects.get(username=slug)
        articles = Article.objects.filter(author=slug)

        user_media = UserProfile.objects.filter(user=slug)[::-1]
        all_user_media = len(user_media)

        all_articles = len(articles)

        return render(request, "startup/author_details.html",
                      {"author": author,
                       "articles": articles,
                       "all_articles": all_articles,
                       "all_user_media": all_user_media})


class AuthorArticlesView(View):
    """Details of article"""

    def get(self, request, slug):
        articles = Article.objects.filter(author=slug)
        author = slug

        return render(request, "startup/author_articles.html",
                      {"articles": articles, "author": author})


class ProfileDetailsView(View):
    """Details of author"""

    def get(self, request):
        users_articles = Article.objects.filter(author=request.user.username)
        all_users_articles = len(users_articles)

        return render(request, "startup/profile.html", {"users_articles": users_articles,
                                                        "all_users_articles": all_users_articles})


def article_create_view(request):
    current_username = request.user

    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form_username = form.cleaned_data.get("author")

        if form_username == str(current_username):
            form.save()
            messages.success(request, "You have created a new article!")
            # form = ArticleForm()
            return redirect("article_list")
        else:
            messages.error(request, "Please, enter your user name")
            form = ArticleForm()

    return render(request, "startup/article_create.html", {"form": form})


def user_media_view(request, slug):
    current_username = request.user

    media = UserMediaForm(request.POST or None)

    if media.is_valid():
        form_username = media.cleaned_data.get("user")

        if form_username == str(current_username):
            media.save()
            messages.success(request, "You have changed info about you!")
            media = UserMediaForm()
        else:
            messages.error(request, "Please, enter your user name")
            media = UserMediaForm()

    return render(request, "startup/user_media.html", {"media": media})


def article_delete_view(request, slug):
    obj = get_object_or_404(Article, url=slug)

    if request.method == "POST":
        obj.delete()
        messages.error(request, "You have deleted an article")
        return redirect("/articles_list")

    return render(request, "startup/article_delete.html", {"object": obj})
