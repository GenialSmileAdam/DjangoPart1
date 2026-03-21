from django.contrib import admin
from . import models

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'membership', 'phone']
    list_editable = ['membership']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']
    
    def first_name(self, obj):
        return obj.user.first_name
    first_name.admin_order_field = 'user__first_name'
    
    def last_name(self, obj):
        return obj.user.last_name
    last_name.admin_order_field = 'user__last_name'
    
    def email(self, obj):
        return obj.user.email
    email.admin_order_field = 'user__email'