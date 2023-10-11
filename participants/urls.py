from django.urls import path

from . import views

urlpatterns = [
    path("participants/", views.ParticipantList.as_view()),
    path("participants/<str:pk>/", views.ParticipantDetail.as_view()),
    path("participants/avg", views.ParticipantListAvg.as_view())
]