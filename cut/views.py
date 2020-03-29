from django.shortcuts import render
from django.views.generic import CreateView
from .forms import Links
from .models import ListLink
from django.db import IntegrityError


def home (request):
    data = {
    'title':'Главная страница сайта'
    }
    return render(request, 'cut/home.html', data )

def about(request):
    data = {'title':'Про нас'}
    return render(request, 'cut/about.html', data )


class CreateShortLink(CreateView):
    model = ListLink
    fields = ['long_link', 'short_link']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['link'] = ListLink.objects.all()
        context['title'] = "Создание ссылки"
        return context
