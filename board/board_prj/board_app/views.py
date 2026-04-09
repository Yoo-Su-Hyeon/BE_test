from django.shortcuts import render, redirect
from .forms import GuestForm
from .models import Guest


def index(request):
    guests = Guest.objects.all()

    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_app:index')
    else:
        form = GuestForm()

    return render(request, 'board_app/index.html', {'form' :form , 'guests':guests})