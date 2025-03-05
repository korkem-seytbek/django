from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, "reservations/reservation_list.html", {"reservations": reservations})

def reservation_create(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reservation_list")
    else:
        form = ReservationForm()
    return render(request, "reservations/reservation_form.html", {"form": form})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, "reservations/reservation_detail.html", {"reservation": reservation})
