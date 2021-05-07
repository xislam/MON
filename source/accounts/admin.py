from urllib.robotparser import Entry

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from django.contrib.auth.admin import GroupAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'role')
        }),
        (_('Additional'), {
            'fields': ('password', 'is_superuser', 'is_staff')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': ('email', 'role', 'password1', 'password2',  'is_superuser', 'is_staff')
        }),
    )
    ordering = 'email',
    list_display = 'email',
    list_filter = 'role',
    search_fields = 'email',

    def change_view(self, request, object_id, form_url='', extra_content=None):
        self.fieldsets = (
            (None, {
                'fields': ('email', 'role', 'is_superuser', 'is_staff')
            }),
            (_('Additional'), {
                'fields': ('password',)
            })
        )
        return super().change_view(request, object_id, form_url, extra_content)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        user = request.user
        if user.role == 'director':
            context['adminform'].form.fields['role'].choices = ('employee', _('employee')),
        return super().render_change_form(request, context, add, change, form_url, obj)
