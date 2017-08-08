"""Admin configuration for core models."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from zoho_reports.core.models import Page, User


class CustomUserAdmin(UserAdmin):
    """Admin configuration for the custom User model."""
    list_display = ('username', 'email', 'full_name', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, CustomUserAdmin)


class PageAdmin(admin.ModelAdmin):
    """Admin configuration for the Page model."""

admin.site.register(Page, PageAdmin)
