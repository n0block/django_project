from django.urls import path
from . import views as submissions_views

urlpatterns = [
    path('', submissions_views.home, name="submissions-home"),
    path('new/', submissions_views.SubmissionCreateView.as_view(), name="submissions-create"),
    path('entries/', submissions_views.SubmissionListView.as_view(), name="submissions-entries"),
    path('about/', submissions_views.about, name='submissions-about'),
    path('entries/<int:pk>', submissions_views.SubmissionDetailView.as_view(), name="submission-detail"),

]
