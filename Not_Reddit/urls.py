from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register_page, name="register_page"),
    path("home/", include("startup.urls")),
    path("", include("django.contrib.auth.urls")),
]

