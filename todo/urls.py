from django.urls import path
from .views import TaskModelView 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tasks', TaskModelView, basename='task')

urlpatterns = router.urls
