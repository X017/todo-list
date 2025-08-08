from .models import Task
from rest_framework.serializers import ModelSerializer 



class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task 
        fields = ['id','name','description','is_completed']
