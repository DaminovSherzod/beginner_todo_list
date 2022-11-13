from django.contrib import admin
from django.urls import path
from todoAPI.views import CreateTask, GetTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/<int:id>/', GetTask.as_view()),
   
    path('api/tasks/', CreateTask.as_view()),
    
    


]
