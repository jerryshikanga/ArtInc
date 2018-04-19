from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Bid
from products.models import Product
from .forms import NewBidForm
from django.http import HttpResponse
from users.models import CustomUser

# Create your views here.
@login_required
def userbids(request):
    user = request.user
    context = {
        'object_list':Bid.objects.filter(user=request.user).order_by('date'),
    }
    return render(request, 'bids/bids_list.html', context)

class  New(LoginRequiredMixin, View):
    """docstring for  New."""
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        form = NewBidForm()
        context = {
            'product' : product,
            'form':form,
        }
        return render(request, 'bids/new_bid.html', context)

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        form = NewBidForm(request.POST)

        if form.is_valid():
            newBid = form.save(commit=False)
            newBid.product = product
            newBid.user =request.user
            customuser = CustomUser.objects.get(user=request.user)

            if newBid.amount < product.price :
                context = {
                    'message':"Bid amount offerred too low",
                    'extras':{
                        'Product : '+newBid.product.name,
                        'Product Price :'+str(product.price),
                        'Bid Amount : %d' % (newBid.amount),
                        'User Balance : '+str(customuser.balance)
                        },
                }
                return render(request, 'bids/messages.html', context)

            elif customuser.balance < newBid.amount:
                context = {
                    'message':"Insufficient Balance",
                    'extras':{
                        'Product : '+newBid.product.name,
                        'Bid Amount : %d' % (newBid.amount),
                        'User Balance : '+str(customuser.balance)
                        },
                }
                return render(request, 'bids/messages.html', context)

            else :
                newBid.save()
                context = {
                    'message':"Bid Successful",
                    'extras':{'Product : '+newBid.product.name, 'Bid Amount : %d' % (newBid.amount)},
                }
                return render(request, 'bids/messages.html', context)
        else :
            context = {
                'product' : product,
                'form':form,
            }
            return render(request, 'bids/new_bid.html', context)
