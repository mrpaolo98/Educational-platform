from django.contrib import admin

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from quiz.models import Answer, Quiz, Question, MCQQuestion, Progress, Sitting


class AnswerInline(admin.TabularInline):
    model = Answer


class QuizAdminForm(forms.ModelForm):
    """
        below is from
        http://stackoverflow.com/questions/11657682/
        django-admin-interface-using-horizontal-filter-with-
        inline-manytomany-field
    """

    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label="Questions",
        widget=FilteredSelectMultiple(
            verbose_name="Questions",
            is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = \
                self.instance.question_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm

    list_display = ('title', 'lesson',)
    list_filter = ('lesson',)
    search_fields = ('description', 'lesson',)


class MCQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'lesson',)
    list_filter = ('lesson',)
    fields = ('content', 'lesson',
              'figure', 'quiz', 'explanation', 'answer_order')

    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)

    inlines = [AnswerInline]


class ProgressAdmin(admin.ModelAdmin):
    """
    to do:
            create a user section
    """
    search_fields = ('user', 'score',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(MCQQuestion, MCQuestionAdmin)
admin.site.register(Progress, ProgressAdmin)
