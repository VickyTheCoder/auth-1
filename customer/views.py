from django.shortcuts import render
from django.http import Http404
from django.contrib import auth
import traceback
# Create your views here.
def add_user(req):
    error = None # Assumes the user creation is positive
    if req.method == 'POST':
        usr = req.POST.get('userid')
        pwd = req.POST.get('password')
        pwd2 = req.POST.get('password2')
        if pwd != pwd2:
            error = "Passwords dont match.." # could be moved to JS
        else:
            # to catch an DB/auth issues
            try:
                user = auth.models.User.objects.create_user(username=usr,
                                    password=pwd)
                if user:# if signup successful?
                    auth.login(req, user) # logins
                    # to check if username is shown in profile page
                    return render(request=req,
                              template_name='profile.html')
                else:
                    error = 'Fill the form carefully'
            except Exception as e:
                print(traceback.format_exc())# to debug
                error = str(e)
    else:
        # to reject all other methods, allows post request alone
        raise Http404("Invalid Request") 
    if error:
        # reloads signup page with proper directions
        return render(request=req,
                              template_name='signup.html',
                              context={'msg': error})
    