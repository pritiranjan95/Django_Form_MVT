from pydoc import visiblename
from django.urls import path
from name import views

urlpatterns = [
    path("", views.index),
    path("contact", views.contact),
    path("home", views.home),
    path("about-us", views.about),
    path("form",views.form, name="formpage"),
    path("Thank-you", views.thanks, name="thankspage")
]