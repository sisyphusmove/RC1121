from django.views.generic import ListView, DetailView, FormView

from photo.models import Album, Photo
from photo.forms import PhotoSearchForm

from django.db.models import Q
from django.shortcuts import render

# Create your views here.


class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo

class SearchFormView(FormView):

    form_class = PhotoSearchForm

    template_name = 'photo/photo_search.html'


    def form_valid(self, form):

        schWord = '%s' % self.request.POST['search_word']

        post_list = Photo.objects.filter(
            Q(title__icontains=schWord)).distinct()


        context = {}

        context = {}

        context['search_term'] = schWord

        context['object_list'] = post_list


        return render(self.request, self.template_name, context)

