from django.contrib import admin
from django.urls import path
from todoAPI.views import (CreateTask, 
                            GetTask, 
                            UpdateTask, 
                            DeleteTask,
                            CompletedTask,
                            IncompletedTask,
                            MaskCompletedTask
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/<int:id>/', GetTask.as_view()),
    path('api/update/<int:id>/', UpdateTask.as_view()),
    path('api/tasks/', CreateTask.as_view()),
    path('api/tasks/delete/<int:id>/', DeleteTask.as_view()),
    path('api/tasks/completed/', CompletedTask.as_view()),
    path('api/tasks/incompleted/', IncompletedTask.as_view()),
    path('api/task/completed/<int:id>/', MaskCompletedTask.as_view()),
    


]
