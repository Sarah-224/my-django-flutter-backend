# my_flutter_app/views.py
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny

class TaskListView(generics.ListCreateAPIView):
    # يسمح لأي مستخدم بالوصول (إذا أردت حماية الـ API، قم بتغيير هذا)
    permission_classes = [AllowAny] 
    
    # تحديد الاستعلام (جلب جميع المهام)
    queryset = Task.objects.all()
    
    # تحديد Serializer (لتنسيق البيانات)
    serializer_class = TaskSerializer

# يمكنك إضافة المزيد من الـ Views هنا لاحقاً (مثل TaskDetailView)