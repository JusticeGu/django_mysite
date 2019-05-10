from django.urls import path
from django.views.generic import TemplateView 
from .views import AboutView, CourseListView, ManageCourseListView, CreateCourseView, DeleteCourseView, CreateLessonView, ListLessonsView, DetailLessonView, StudentListLessonView

app_name = "course" 

urlpatterns = [
    #path('about/', TemplateView.as_view(template_name="course/about.html")),
     ]
