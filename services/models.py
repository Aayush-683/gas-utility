from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class ServiceRequest(models.Model):
    requestTypes = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
    ]

    statuses = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests')
    requestType = models.CharField(max_length=20, choices=requestTypes)
    description = models.TextField()
    fileAttachment = models.FileField(upload_to='static/attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=statuses, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'is_staff': True},  # Only staff members can be assigned
        related_name='assigned_requests'
    )

    def __str__(self):
        return f"{self.customer.username} - {self.requestType} - {self.status}"
