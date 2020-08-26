from django.db import models

from datetime import date

from django.urls import reverse


class Preferences(models.Model):
    category = models.CharField("Category", max_length=150, unique=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Gender(models.Model):
    category = models.CharField("Gender", max_length=150, unique=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = "Gender"


class ArticleColor(models.Model):
    theme = models.CharField("Theme", max_length=50, unique=True)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"


class Article(models.Model):
    title = models.CharField("Title", max_length=150, unique=True)
    description = models.TextField("Description")
    category = models.ForeignKey(Preferences, on_delete=models.CASCADE, related_name="Category")
    author = models.CharField("Author", max_length=50)
    date = models.DateField("Date of writing", default=date.today)
    color = models.ForeignKey(ArticleColor, on_delete=models.CASCADE, related_name="Theme")
    url = models.SlugField(max_length=150, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.url:
            slug_string = ""
            for discard in str(self.title).lower():
                if discard.isalpha() or discard.isdigit() or discard == " ":
                    slug_string += discard
                continue
            slug_list = [letter for letter in slug_string.lower().split()]

            self.url = "_".join(slug_list)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_details", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comments(models.Model):
    description = models.TextField("Description", max_length=150)
    articles_name = models.CharField("Articles name", max_length=150)
    author = models.CharField("Author", max_length=50)

    def save(self, *args, **kwargs):
        slug_string = ""
        for discard in str(self.articles_name).lower():
            if discard.isalpha() or discard.isdigit() or discard == " ":
                slug_string += discard
            continue
        slug_list = [letter for letter in slug_string.lower().split()]

        self.articles_name = "_".join(slug_list)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class UserProfile(models.Model):
    user = models.CharField("User", max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="Gender")
    preference_category = models.ForeignKey(Preferences, on_delete=models.CASCADE, related_name="Preference")
    facebook = models.URLField("Facebook", max_length=200, blank=True)
    instagram = models.URLField("Instagram", max_length=200, blank=True)
    twitter = models.URLField("Twitter", max_length=200, blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Preference"
        verbose_name_plural = "Preferences"
