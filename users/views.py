from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .forms import LoginForm, UserUpdateForm, UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate, logout, login, tokens
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

class Detail(generic.DetailView):
    """docstring for Detail."""
    model = CustomUser
    context_object_name = 'customuser'
    template_name = "users/customuser_detail.html"

class UsersList(LoginRequiredMixin, generic.ListView):
    model = CustomUser
    template_name = "users/customuser_list.html"

class Login(View):
    """docstring for Login."""
    def get(self, request):
        form = LoginForm()
        context = {
            'form':form,
        }
        return render(request, "users/login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else :
                    return redirect(reverse('users:profile',  args=[request.user.id]))
            else :
                messageText = "Invalid username or password"
                context = {
                    'form':form,
                    'messageText':messageText,
                }
                return render(request, "users/login.html", context)
        else :
            context = {
                'form':form,
            }
            return render(request, "users/login.html", context)
        return render(request, "users/login.html")

class PasswordReset(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_url = reverse_lazy('users:login')
    # html_email_template_name = 'users/password_reset_email.html'

class PasswordResetConfirm (PasswordResetConfirmView):
    """docstring for PasswordResetConfirm ."""
    template_name = 'users/password_reset_confirm'
    success_url = reverse_lazy('users:password_reset_complete')

class  PasswordResetComplete(PasswordResetCompleteView):
    """docstring for  PasswordResetComplete."""
    template_name = 'users/password_reset_complete.html'

class Register(View):
    def get(self, request):
        form = UserCreationForm()
        context = {
            'form':form,
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            authuser = form.save()
            authuser.refresh_from_db()
            authuser.customuser.website = form.cleaned_data.get('website')
            authuser.customuser.telephone = form.cleaned_data.get('telephone')

            login(request, authuser)
            return redirect('/users/user/%d'%(authuser.id))
        else :
            context = {
                'form':form,
            }
            return render(request, 'users/register.html', context)

class Update(LoginRequiredMixin, generic.UpdateView):
    context_object_name = 'customuser'
    model = CustomUser
    fields = ['website', 'picture', 'telephone', ]
    # form_class = UserUpdateForm
    template_name_suffix =  '_update_form'
    success_url = reverse_lazy('home:dashboard')

class Edit(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        customuser = get_object_or_404(CustomUser, user=user)
        initialData = {
            'website':customuser.website,
            'picture':customuser.picture,
        }
        form = UserUpdateForm(initialData)
        context = {
            'customuser' : customuser,
            'form':form,
        }
        return render(request, 'users/editProfile.html', context)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        customuser = get_object_or_404(CustomUser, user=user)
        form=UserUpdateForm(request.POST)
        if form.is_valid():
            customuser.website = form.cleaned_data['website']
            customuser.picture = form.cleaned_data['picture']
            customuser.save()
            return redirect(reverse('users:editSuccess'))
        else:
            context = {
                'customuser' : customuser,
                'form':form,
            }
            return render(request, 'users/editProfile.html', context)

def editSuccess(request):
    return render(request, 'users/editSuccess.html')

def logoutUser(request):
    logout(request)
    return redirect(reverse('users:login'))

class PasswordResetDone(PasswordResetDoneView):
    """docstring for PasswordResetDone."""
    template_name = 'users/password_reset_done.html'
