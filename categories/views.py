from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from .models import Category

# Create your views here.
class  List(ListView):
    """docstring for  List."""
    model = Category

class UpdateCategory(UpdateView):
    model = Category
    template_name_suffix = '_update_form'
    fields = ['name', 'description']
    success_url = reverse_lazy('categories:edit_category_success')

class CreateCategory(CreateView):
    """docstring for CreateCategory."""
    model = Category
    template_name_suffix  = '_create_form'
    fields = ['name', 'description']
    success_url = reverse_lazy('categories:add_category_success')


class Detail(DetailView):
    """docstring for Detail."""
    model = Category
    context_object_name = 'category'

class Messages(View):
    def get(self, request, *args, **kwargs):
        message = ""
        if kwargs['type'] == 'add_category_success':
            message = 'Category Added Successfully'
        elif kwargs['type'] == 'edit_category_success':
            message = 'Category edited successfully'

        context = {
            'message':message
        }
        return render(request, 'home/messages.html', context)
