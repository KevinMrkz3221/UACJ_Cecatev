from rest_framework.serializers import ModelSerializer
from .models import FormType, Question

class FormTypeSerializer(ModelSerializer):
    class Meta:
        model = FormType
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'