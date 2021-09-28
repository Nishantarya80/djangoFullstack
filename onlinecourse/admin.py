from django.contrib import admin
from django.db.models.base import Model
# <HINT> Import any new Models here
from .models import Choice, Course, Lesson, Instructor, Learner, Qusetion

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInline(admin.StackedInline):
    model = Qusetion
    extra = 3

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Qusetion,QuestionAdmin)
admin.site.register(Choice)