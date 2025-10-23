from rest_framework import serializers 
from .models import Task 
class TaskSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Task 
        fields = ('id', 'title','completed') # الحقول التي سيراها Flutter 
        read_only_fields = ('created_at', 'updated_at') # الحقول التي لا يمكن تعديلها