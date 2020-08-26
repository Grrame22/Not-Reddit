from django import forms

from .models import Article, UserProfile, Comments
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ArticleForm(forms.ModelForm):
    captcha = ReCaptchaField()

    title = forms.CharField(label="Title",
                            widget=forms.TextInput(attrs={"placeholder": "Your title", "class": "form-control"}))
    description = forms.CharField(label="Description", max_length=3000,
                                  widget=forms.Textarea(attrs={"placeholder": "Your description",
                                                               "rows": 20, "cols": 60, "class": "form-control"}))
    category = forms.CharField(label="Category"),
    color = forms.CharField(label="Color theme"),
    author = forms.CharField(label="Username",
                             widget=forms.TextInput(attrs={"placeholder": "Your name", "class": "form-control"}))

    class Meta:
        model = Article
        fields = ["title",
                  "description",
                  "category",
                  "color",
                  "author",
                  "captcha"]


class CommentsForm(forms.ModelForm):
    description = forms.CharField(label="Description", max_length=150,
                                  widget=forms.Textarea(attrs={"placeholder": "Your description",
                                                               "rows": 2, "cols": 70, "class": "form-control"}))

    author = forms.CharField(label="Username", max_length=50,
                             widget=forms.TextInput(attrs={"placeholder": "Your name", "class": "form-control"}))

    articles_name = forms.CharField(label="Article name", max_length=150,
                                    widget=forms.TextInput(
                                        attrs={"placeholder": "Articles name", "class": "form-control"}))

    class Meta:
        model = Comments
        fields = ["description",
                  "author",
                  "articles_name"]


class UserMediaForm(forms.ModelForm):
    user = forms.CharField(label="Username",
                           widget=forms.TextInput(attrs={"placeholder": "Your name", "class": "form-control"})),
    preference_category = forms.CharField(label="Preferences"),
    gender = forms.CharField(label="Gender"),
    facebook = forms.URLField(label="Facebook",
                              widget=forms.TextInput(attrs={"placeholder": "Your link", "class": "form-control"}),
                              required=False)
    instagram = forms.URLField(label="Instagram",
                               widget=forms.TextInput(attrs={"placeholder": "Your link", "class": "form-control"}),
                               required=False)
    twitter = forms.URLField(label="Twitter",
                             widget=forms.TextInput(attrs={"placeholder": "Your link", "class": "form-control"}),
                             required=False)

    class Meta:
        model = UserProfile
        fields = ["user",
                  "gender",
                  "preference_category",
                  "facebook",
                  "instagram",
                  "twitter"]
