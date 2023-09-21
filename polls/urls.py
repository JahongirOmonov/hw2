from django.urls import path
from .views import YaratishView, AllSee, PatchStatus



urlpatterns=[
    path('YaratishView/', YaratishView.as_view()),
    path('AllSee/', AllSee.as_view()),
    path('PatchStatus/<int:forid>', PatchStatus.as_view()),
]