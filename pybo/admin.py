from django.contrib import admin
from pybo.models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question)
admin.site.register(Answer)
