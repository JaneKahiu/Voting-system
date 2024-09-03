from django.contrib import admin
from .models import Question, Choice, Vote

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'created_at')
    search_fields = ['question_text']
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')
    search_fields = ('choice_text',)
    list_filter = ('question',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote)