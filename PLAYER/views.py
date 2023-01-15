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

