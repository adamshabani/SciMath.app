from django.contrib import admin
from. import models

# Register your models here.


@admin.register(models.category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
    actions = ['delete_model']
    
@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title'
    ]
        
class AnswerInlineModel(admin.TabularInline):
    model = models.Answers
    fields = [
        'answer_text',
        'is_right'
    ]
  
@admin.register(models.Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = [
    
        'question',
        'answer_text',
        'is_right',
        
    ]  
    
@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    
    list_display = [
        'title',
        'quiz',
        'date_created',
        'Level',
    ]
    fields =[
        'subject_name',
        'topic',
        'Level',
        'title',
        'quiz',
        
        
        
    ]
    inlines = [
        AnswerInlineModel,
    ]