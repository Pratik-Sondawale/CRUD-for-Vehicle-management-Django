from django.shortcuts import render, get_object_or_404, redirect
from .forms import VehicleForm
from .models import Vehicle

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

def vehicle_create(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_form.html', {'form': form})

def vehicle_update(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_form.html', {'form': form, 'vehicle': vehicle})

def vehicle_delete(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_confirm_delete.html', {'vehicle': vehicle})
