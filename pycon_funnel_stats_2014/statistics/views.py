from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from urllib2 import urlopen
import program

def stats(request):
	html = urlopen('http://in.pycon.org/funnel/2014/')
	page = html.read()
	total = program.total(page)
	proposallist = program.proposallist(page)
	return render_to_response("home.html",{'total':total, 'begineer':proposallist[0], 'intermediate':proposallist[1], 'advanced':proposallist[2]})