from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'requestType', 'status', 'created_at')
    list_filter = ('status', 'requestType')
    search_fields = ('customer__username', 'description')
