from django.shortcuts import render, get_object_or_404
from .models import Parcel

def parcel_list(request):
    parcels = Parcel.objects.all()
    return render(request, 'parcel/parcel_list.html', {'parcels': parcels})

def receive_parcel(request, pk):
    parcel = get_object_or_404(Parcel, pk=pk)
    parcel.status = 'Received'
    parcel.received_at = timezone.now()
    parcel.save()
    return render(request, 'parcel/parcel_detail.html', {'parcel': parcel})
