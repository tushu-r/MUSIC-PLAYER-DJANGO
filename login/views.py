from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect ,request 
from django.shortcuts  import render

from . import views 
from django.db import models
from signup import models as md 

from django.template import Template , Context 
import os 

from django.contrib import admin


def login(request , error):
    return render(request ,'login/login.html'  )



def logincheck(request , error):
    if(error == '0' or error == '1'):

        if( request.GET['username'] != "" and  request.GET['email'] != ""  ):
            username =  request.GET['username'] 
            email = request.GET['email']
            try: 
                if( username  == md.USER.objects.get( username = username ).username   and
                email  ==  md.USER.objects.get( username = username).email):
                    
                    no = md.USER.objects.get(username = username)
                    no = no.no 
                    
                    return redirect(f'/muvid/{no}')
            except:
               return redirect('/signup/signup/01' )
        else:
            data = {
                'please':"NAME AND EMAIL ARE REQUIRED" 
            }
            return redirect('login/1/' , data)
             

           
                 
             
                 
    
             
    
       

        



    
    
    
   
    