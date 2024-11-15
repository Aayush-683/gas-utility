from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from .models import ServiceRequest
from .forms import ServiceRequestForm, UserRegistrationForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            # Save the attachment file if it exists
            if 'fileAttachment' in request.FILES:
                service_request.fileAttachment = request.FILES['fileAttachment']
                # Save file locally in the 'attachments' directory
                service_request.save()
            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit.html', {'form': form})

@login_required
def track_requests(request):
    if request.user.is_staff:
        return redirect('support_dashboard')
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'services/track.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    return render(request, 'services/reqDetails.html', {'service_request': service_request})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('track_requests')  # Redirect to track requests page
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def is_support_staff(user):
    return user.is_staff  # Only staff/admin users can access the dashboard

@user_passes_test(is_support_staff)
def support_dashboard(request):
    # Get all service requests
    requests = ServiceRequest.objects.all()

    # Filter by pending, in-progress, or resolved status
    status_filter = request.GET.get('status')
    if status_filter:
        requests = requests.filter(status=status_filter)

    return render(request, 'services/supportDash.html', {'requests': requests})

@user_passes_test(is_support_staff)
def update_request_status(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        service_request.status = new_status

        # Assign the request to the logged-in support member if status is in-progress
        if new_status == 'in_progress':
            service_request.assigned_to = request.user
        elif new_status == 'resolved':
            service_request.assigned_to = request.user
        elif new_status == 'pending':
            service_request.assigned_to = None

        service_request.save()
        return redirect('support_dashboard')

    return render(request, 'services/handleReq.html', {'service_request': service_request})