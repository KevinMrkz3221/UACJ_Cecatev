from django.contrib import admin
from .models import FormType, Question, Answer
# Register your models here.
class FormTypeAdmin(admin.ModelAdmin):
    model = FormType
    list_display = ('name', 'is_active')

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ('form_type', 'question', 'is_active')

class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ('question', 'answer')

admin.site.register(FormType, FormTypeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)