from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View, generic
from .forms import ProductForm
from .models import Product, Category
from bids.models import Bid
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, Max
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from bids.models import Bid
from django.db.models import Max, Min, Avg

# Create your views here.
class DetailView(generic.DetailView):
    model = Product
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bids'] = Bid.objects.filter(product=self.object)
        return context

class ProductsList(generic.ListView):
    model = Product

def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    object_list = Product.objects.filter(category=category).annotate(Count('bid'), Max('bid__amount'))
    context = {
        'object_list':object_list,
        'category':category.name,
    }
    return render(request, 'products/product_list.html', context)

class Create(PermissionRequiredMixin, CreateView):
    permission_required = 'products.can_add'
    permission_required_message = "You don't have permissions to add a product. Login with an authorised account"
    model = Product
    template_name_suffix = '_create_form'
    fields = ['user', 'name', 'category', 'price', 'description', 'photo']
    success_url = reverse_lazy('products:addSuccess')

class Update(UpdateView):
    model = Product
    template_name_suffix = '_update_form'
    fields = ['user', 'name', 'category', 'price', 'description', 'photo']
    success_url = reverse_lazy('products:editSuccess')

class Messages(View):
    def get(self, request, *args, **kwargs):
        message = ""
        if kwargs['type']=='editSuccess':
            message = 'Edit success'
        elif kwargs['type']=='addSuccess':
            message = 'Add success'
        elif kwargs['type'] == 'add_category_success':
            message = 'Category Added Successfully'
        elif kwargs['type'] == 'edit_category_success':
            message = 'Category edited successfully'

        context = {
            'message':message
        }
        return render(request, 'products/messages.html', context)

class Search(View):
    def post(self, request):
        key = request.POST.get('searchquery')
        product_list = Product.objects.filter(name__icontains=key)
        context = {
            'object_list':product_list,
            'key':key,
        }
        return render(request, 'products/product_list.html', context)

def checkout(request, pk):
    product = get_object_or_404(Product, pk=pk)
    bid_amount = product.bid__amount__max
    bid  = Bid.objects.get(product=product, amount=bid_amount)
    bid.success = True
    bid.save()
    product.active = False
    product.save()
    context = {
        'product':product,
        'bid' : bid,
    }
    return render(request, "products/checkout.html", context)
