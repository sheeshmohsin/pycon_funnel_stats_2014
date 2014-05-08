from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import Context
from urllib2 import urlopen
import program

def stats(request):
    html = urlopen('http://in.pycon.org/funnel/2014/')
    page = html.read()
    total = program.total(page)
    proposallist = program.proposallist(page)
    section = program.section(page)
    beginnerlist = program.beginner(page)
    context = Context({'total':total, 'begineer':proposallist[0],
            'intermediate': proposallist[1],'advanced':proposallist[2], 
            'beginnerchart': section[0], 'intermediatechart': section[1], 
            'advancedchart': section[2], 'beginners' : beginnerlist})
    return render_to_response("home.html", context)