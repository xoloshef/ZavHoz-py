from django.contrib import admin

from .models import Question, Choice, Workers, Assets, BaseActs

# принимет до трех вот все модели: Question, Choice, Workers, Assets, BaseActs

admin.site.register(BaseActs)
admin.site.register(Workers)
admin.site.register(Assets)
admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(QuestionAdmin)
