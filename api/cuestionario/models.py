from django.db import models

# Create your models here.
class FormType(models.Model):
    name = models.CharField(max_length = 200, verbose_name='name')
    is_active = models.BooleanField(default=True, verbose_name='is_active')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Form Type'
        verbose_name_plural = 'Form Types'
        db_table = 'form_type'

class Question(models.Model):
    form_type = models.ForeignKey(FormType, on_delete=models.PROTECT)
    question = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.question
    
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'question'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.BooleanField()
    observations = models.TextField()

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answer'