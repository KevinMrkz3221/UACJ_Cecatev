from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FormTypeViewSet, QuestionViewSet

router = DefaultRouter()

router.register('form_types', FormTypeViewSet, 'form_types')
router.register('questions', QuestionViewSet, 'questions')

urlpatterns = [
    path('', include(router.urls)),
]