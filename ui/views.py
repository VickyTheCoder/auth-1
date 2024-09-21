from django.shortcuts import render
from django.http import Http404

# Create your views here.
def homepage(req):
    if req.method == 'GET':
        return render(request=req,
                      template_name='index.html')
    raise Http404("Invalid Request")

def register(req):
    if req.method == 'GET':
        return render(request=req,
                      template_name='signup.html')
    raise Http404("Invalid Request")