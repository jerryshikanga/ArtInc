from django.shortcuts import render
from bids.models import Bid
from products.models import Product
from users.models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    test = ''
    context = {
        'bids': Bid.objects.all().order_by('date')[:10],
        'users': CustomUser.objects.all().order_by('user__date_joined')[:8],
        'bidsNum': Bid.objects.all().count(),
        'usersNum': CustomUser.objects.all().count(),
        'products': Product.objects.all().order_by('date')[:10],
        'productsNum':Product.objects.all().count(),
    }
    return render(request, 'home/index.html', context)
