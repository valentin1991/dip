from django.shortcuts import render
from django.views.generic import CreateView
from .forms import Links
from .models import ListLink





def home (request):
    data = {
    'title':'Главная страница сайта'
    }
    return render(request, 'cut/home.html', data )


class CreateShortLink(CreateView):
    model = ListLink
    fields = ['long_link', 'short_link']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['link'] = ListLink.objects.all()
        return context

    # def shortlink (request):
    #     data = {'link': ListLink.objects.all()}
    #     return render(request, 'cut/listlink_form.html', data )


# class DisplayLink(DetailView):
#
#     model = ListLink
#
#     def get_context_data(self, **kwargs):
#         context = super(DisplayLink, self).get_context_data(**kwargs)
#         context['list'] = ListLink.objects.all()
#         return context
#



# def shortlink (request):
#     data = {'link': ListLink.objects.all()}
#     return render(request, 'cut/listlink_form.html', data )
#
#


# def shortlink (request):
#     if request.method == "POST":
#         avtor = self.request.user
#         long_link = LongLink(request.POST, instance = request.user.profile)
#         short_link =
#
#
#
#     short = ShortLink()
#     long = LongLink()
#     data = {
#     'title':'Сокращатель',
#     'long': long,
#     'short': short,
#     'link': ListLink.objects.all(),
#     }
#
#     return render(request, 'C:\Users\Valentin\Desktop\dip', data )
