from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'home.html')

#top up views
@login_required
def topup(request):
    return render(request, 'topup.html')

@login_required
def topup_9mobile(request):
    return render(request, 'topup-9mobile.html')

@login_required
def topup_airtel(request):
    return render(request, 'topup-airtel.html')

@login_required
def topup_glo(request):
    return render(request, 'topup-glo.html')

@login_required
def topup_mtn(request):
    return render(request, 'topup-mtn.html')

# electricity views
@login_required
def electricity(request):
    return render(request, 'electricity.html')

@login_required
def electricity_aedc(request):
    return render(request, 'electricity-aedc.html')

# tv views
@login_required
def tv(request):
    return render(request, 'tv.html')

@login_required
def tv_dstv(request):
    return render(request, 'tv-dstv.html')

@login_required
def tv_gotv(request):
    return render(request, 'tv-gotv.html')

@login_required
def tv_startimes(request):
    return render(request, 'tv-startimes.html')

# travel views
@login_required
def travel(request):
    return render(request, 'travel.html')

@login_required
def travel_9jair(request):
    return render(request, 'travel-9jair.html')

@login_required
def travel_nrc(request):
    return render(request, 'travel-nrc.html')

# hotel views
@login_required
def hotel(request):
    return render(request, 'hotel.html')

@login_required
def hotel_sheraton(request):
    return render(request, 'hotel-sheraton.html')

