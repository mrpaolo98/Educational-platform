from django import forms

from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory, RadioSelect

from .models import user_registrated, SubRubric, SuperRubric, Lesson, \
    AdditionalFile, Comment
from .models import AdvUser
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group

User = get_user_model()

# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html()
    )

    password2 = forms.CharField(
        label='Пароль (повторно)',
        widget=forms.PasswordInput,
        help_text='Введите тот же самьй! пароль еще раз для проверки'
    )

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registrated.send(RegisterUserForm, instance=user)
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'send_messages')


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name')


class SubRubricForm(forms.ModelForm):
    super_rubric = forms.ModelChoiceField(
        queryset=SuperRubric.objects.all(), empty_label=None,
        label='Надрубрика', required=True)

    class Meta:
        model = SubRubric
        fields = '__all__'


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='')


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}


AIFormSet = inlineformset_factory(Lesson, AdditionalFile, fields='__all__')


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'lesson': forms.HiddenInput, 'author': forms.HiddenInput}


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)
