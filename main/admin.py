import datetime

from django.contrib import admin
from django.contrib.auth.models import Group

from main.forms import SubRubricForm, GroupAdminForm
from .utilities import send_activation_notification
from .models import AdvUser, SubRubric, SuperRubric, AdditionalFile, Lesson, \
    Comment, GroupStudents, Crew, CourseProject


def send_activation_notifications(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, 'Письма с оповещениями отправлены')


send_activation_notifications.short_description = 'Отправка писем с ' + \
                                                  'оповещениями об активации'


class NonactivatedFilter(admin.SimpleListFilter):
    title = 'Прошли активацию?'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Прошли'),
            ('threedays', 'Не прошли более 3 дней'),
            ('week', 'Не прошли более недели'),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False,
                                   date_joined__date__lt=d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False,
                                   date_joined__date__lt=d)


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonactivatedFilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('send_messages', 'is_active', 'is_activated'),
              ('is_staff', 'is_superuser', 'is_teacher'),
              'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications,)


admin.site.register(AdvUser, AdvUserAdmin)


class SubRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric', 'description')
    inlines = (SubRubricInline,)


admin.site.register(SuperRubric, SuperRubricAdmin)


class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm


admin.site.register(SubRubric, SubRubricAdmin)


class AdditionalFileInline(admin.TabularInline):
    model = AdditionalFile


class LessonAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'author', 'created_at')
    fields = (('rubric', 'author'), 'order', 'title', 'video', 'content',
              'contacts', 'is_active')
    inlines = (AdditionalFileInline,)


admin.site.register(Lesson, LessonAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'lesson', 'created_at')
    fields = (('lesson', 'author'), 'content', 'is_active')


admin.site.register(Comment, CommentAdmin)

# Unregister the original Group admin.
admin.site.unregister(Group)


# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)

admin.site.register(GroupStudents)
admin.site.register(Crew)
admin.site.register(CourseProject)
