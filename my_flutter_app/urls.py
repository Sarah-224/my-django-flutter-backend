# my_flutter_app/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # هذا هو مسار المهام الفعلي (سيصبح المسار الكامل: /api/tasks/)
    path('tasks/', views.TaskListView.as_view(), name='task-list'), 
]

urlpatterns = format_suffix_patterns(urlpatterns)