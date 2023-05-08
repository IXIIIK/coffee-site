from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

menu = ['Home', 'Menu', 'About Us', 'Our Story', 'Blog', 'Contact']

def index_page(request):
    context = {
        'title': 'Coffee-Site',
        'menu': menu
    }
    return render(request, 'index.html', context)

class SignUP(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
