from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import *

from bashoneliners.main.models import Hacker


''' constants '''

#


''' url handlers '''

def index(request):
    params = {
	    }
    return render_to_response('main/index.html', params)

def oneliner(request, pk):
    return index(request)


# eof