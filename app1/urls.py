from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    # path('books/',views.hello),
    path('books/',views.books),
    path('book/<str:inp>',views.BookView.as_view()), #int||str
]
