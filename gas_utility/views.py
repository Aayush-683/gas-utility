from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def home(request):
    return redirect('submit_request')

@login_required
def account(request):
    user = request.user
    return render(request, 'account.html', {'user': user})