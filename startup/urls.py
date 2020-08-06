from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home_page"),
    path("article_create/", views.article_create_view, name="article_create"),
    path("comment_create/<slug:slug>/", views.comments_article_view, name="comment_create"),
    path("article_delete/<slug:slug>/", views.article_delete_view, name="article_delete"),
    path("about/", views.AboutPageView.as_view(), name="about_page"),
    path("team/", views.TeamPageView.as_view(), name="team_page"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts_page"),
    path("profile/", views.ProfileDetailsView.as_view(), name="profile_page"),
    path("profile/<slug:slug>/", views.ProfileDetailsView.as_view(), name="profile_page"),
    path("media/<slug:slug>/", views.UserMediaView.as_view(), name="user_media_page"),
    path("media_create/<slug:slug>/", views.user_media_view, name="media_page"),
    path("articles_list/", views.ArticlesViews.as_view(), name="article_list"),
    path("category_list/", views.CategoriesView.as_view(), name="category_list"),
    path("category/<int:id>/", views.ParticularCategoryView.as_view(), name="category_article_list"),
    path("article/<slug:slug>/", views.ArticleDetailsView.as_view(),
         name="article_details"),
    path("author/<slug:slug>/", views.AuthorDetailsView.as_view(),
         name="author_details"),
    path("author_articles/<slug:slug>/", views.AuthorArticlesView.as_view(),
         name="author_articles"),
]
