from django.contrib import admin
from django.urls import path,include

from studentapp import views

urlpatterns = [path("school/all/",views.school_list),
               path("students/all/",views.StudentListView.as_view()),
               path("school/<int:pk>/",views.school_detail),
               path("student/<int:pk>/",views.StudentDetailView.as_view())

]
