from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from urllib2 import urlopen
import program

def stats(request):
	return render_to_response("home.html",{'total':8, 'begineer':2, 'intermediate':3, 'advanced':5})