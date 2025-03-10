from django.shortcuts import redirect
from .forms import CustomSignUpForm
from allauth.account.views import SignupView
from django.contrib.auth.models import AnonymousUser
from django.views.generic import ListView, DetailView
from .models import Song
from django.contrib.auth.models import User


class SongList(ListView):
    model = Song
    context_object_name = 'songs'
    template_name = 'play/song_list.html'
    def get_queryset(self):
        return  Song.objects.all()
    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super().get_context_data(**kwargs)
        if not (isinstance(self.request.user, AnonymousUser)):
            context['available_songs'] = Song.objects.exclude(favorite_by=self.request.user.pk)
            context['user'] = User.objects.get(id=self.request.user.pk)
            context['favorite_songs_count'] = User.objects.get(id=self.request.user.pk).favorite_songs.all().count()
            context['favorite_songs'] = User.objects.get(id=self.request.user.pk).favorite_songs.all()
        return context

    def post(self, request, *args, **kwargs):
        song_id = request.POST.get('song_id')
        request.user.favorite_songs.add(Song.objects.get(id=song_id))
        return redirect(to='song-list')


class SongDetail(DetailView):
    template_name = 'play/play_page.html'
    context_object_name = 'song'
    def get_queryset(self):
        return Song.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorite_by'] = Song.objects.get(pk=self.object.pk).favorite_by.all()
        return context


class CostumeSignUp(SignupView):
    template_name = 'account/signup.html'

    def get_form_class(self):
        return CustomSignUpForm



