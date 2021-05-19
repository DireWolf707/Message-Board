from django.urls import path
from .views import MessageApiView
urlpatterns = [
    path('',MessageApiView.as_view(),name='api')
]
