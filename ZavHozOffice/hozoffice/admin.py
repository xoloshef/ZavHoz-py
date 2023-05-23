from django.contrib import admin

from .models import Question, Workers, Assets, BaseActs

# принимет до трех вот все модели: Question, Choice, Workers, Assets, BaseActs

admin.site.register(Question)
admin.site.register(Workers)
admin.site.register(Assets)
admin.site.register(BaseActs)

# Register your models here.
