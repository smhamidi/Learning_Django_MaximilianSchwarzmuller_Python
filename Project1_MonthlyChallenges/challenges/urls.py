from django.urls import path

from . import views

urlpatterns = [
    path("", views.challengePage, name="index"),
    path("<int:month>", views.monthChallengeByNumber),
    path("<str:month>", views.monthChallenge, name="month-challenge"),
]
