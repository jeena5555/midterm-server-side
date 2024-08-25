from django.urls import path

from . import views

from .views import *  # Import your view class

urlpatterns = [
    path("", EmployeeView.as_view(), name='employee'),
    path("position/", PositionView.as_view(), name='position'),
    path("project/", ProjectView.as_view(), name='project'),
    path("project/<int:id>/", ProjectDetailView.as_view(), name='project_detail'),
    # path("project/", views.project, name="project"),
    # path("project/delete/<int:id>/", view.delete_project, name="delete_project")
    # path("articles/2003/", views.special_case_2003),
    # path("articles/<int:year>/", views.year_archive),
    # path("articles/<int:year>/<int:month>/", views.month_archive),
    # path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
]
