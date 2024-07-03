from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(Application)
admin.site.register(Answer)

