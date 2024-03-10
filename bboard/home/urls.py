from django.urls import path

from .views import index, rubric_bbs

urlpatterns = [
    path('', index, name='home'),
    path('<int:rubric_id>/', rubric_bbs, name='rubric'),
]