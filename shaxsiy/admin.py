from django.contrib import admin
from .models import Kasblar
# Register your models here.

from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = Kasblar
    list_display = ("username", "is_staff", "is_active", "vazifalari")
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "vazifalari"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(Kasblar, CustomUserAdmin)
