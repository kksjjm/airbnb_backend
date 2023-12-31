from django.urls import path
from . import views

urlpatterns = [
    path("", views.Experiences.as_view()),
    path("<int:pk>", views.ExperiencesDetail.as_view()),
    path("<int:pk>/perks", views.PerksInExp.as_view()),
    path("<int:pk>/bookings", views.BookingsInExp.as_view()),
    path("<int:pk>/bookings/<int:book_pk>", views.BookingDetailInExp.as_view()),
    path("perks", views.Perks.as_view()),
    path("perks/<int:pk>", views.PerkDetail.as_view()),
]
