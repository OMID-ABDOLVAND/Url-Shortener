from django.contrib import admin
from django.contrib.auth import get_user_model

user = get_user_model()


@admin.register(user)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff')
    list_editable = ('is_active', 'is_superuser', 'is_staff')
    search_fields = ('email',)
