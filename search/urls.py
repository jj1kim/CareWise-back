from django.urls import path
from .views import CarelabelSearchView

app_name = 'search'
urlpatterns = [
    path("", CarelabelSearchView.as_view()),
]
