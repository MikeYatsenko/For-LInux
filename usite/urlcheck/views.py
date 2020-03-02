from django.urls import reverse_lazy
from django.views.generic import ( ListView, DetailView, CreateView,UpdateView, DeleteView,)
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import AuthUserForm, URLAddForm
from .models import URL



class URLListView(ListView):
    model = URL
    template_name = 'urlcheck/url_list.html'
    context_object_name = 'url_list'
    queryset = URL.objects.all()

class UsiteLoginView(LoginView):
    model = User
    template_name = 'urlcheck/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('url_list')

class URLCreateView(CreateView):
    model = URL
    form_class = URLAddForm
    template_name = 'urlcheck/url_add_form.html'
    success_url = reverse_lazy('url_list')

class URLDeleteView(DeleteView):
    model = URL
    success_url = reverse_lazy('url_list')
