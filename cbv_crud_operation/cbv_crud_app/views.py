from django.shortcuts import render
from .forms import TeamDetailForm
from .models import TeamDetail
from django.views.generic import UpdateView, RedirectView, DeleteView, ListView, DetailView,TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class HomeTemplate(TemplateView):
    template_name = 'team_detail/home.html'


class TeamDetailListView(ListView):
    model = TeamDetail
    template_name = 'team_detail/list_data.html'
    context_object_name = 'team_detail_list_data'
    

class TeamDetailDetailView(DetailView):
    model = TeamDetail
    template_name = 'team_detail/detail_data.html'
    context_object_name = 'team_detail_detail_data'


class TeamDetailCreateView(CreateView):
    model = TeamDetail
    form_class = TeamDetailForm
    template_name = 'team_detail/create_data.html'

    success_url = reverse_lazy('list_data')


class TeamDetailUpdateView(UpdateView):
    model = TeamDetail
    form_class = TeamDetailForm
    template_name = 'team_detail/create_data.html'
    success_url = reverse_lazy('list_data')


class TeamDetailDeleteView(DeleteView):
    model = TeamDetail
    template_name = 'team_detail/delete_data.html'
    success_url = reverse_lazy('list_data')
