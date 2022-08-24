from django.urls import path
from corporations.views import (
    SearchView,
    RecruitmentView,
    RecruitmentDetailView
)

urlpatterns = [
    path('', RecruitmentView.as_view()),
    path('url', SearchView.as_view()),
    path('<recruitment_id>', RecruitmentView.as_view()),
    path('detail/<recruitment_id>', RecruitmentDetailView.as_view()),
]
