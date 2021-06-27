from django.shortcuts import render
from django.views import generic
from .models import Event, Note, Team
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):

    num_events=Event.objects.all().count()
    num_members=Team.objects.all().count()

    context={
    'num_events':num_events,
    'num_members':num_members,
    }
    return render(request,'index.html',context=context)

class ClubEventsView(LoginRequiredMixin,generic.ListView):
    model=Event


class EventDetailView(LoginRequiredMixin,generic.DetailView):
    model=Event
# Create your views here.
