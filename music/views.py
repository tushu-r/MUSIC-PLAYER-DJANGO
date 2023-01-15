from django.shortcuts import render
from signup import models as md
import os 
import requests



# Create your views here.

def create(request , no ):
    x = md.USER.objects.get(no = no)

    username = x .username 
    directory = x.directory

    
    songs_list = os.listdir(f"C:\\Users\\joece\\PycharmProjects\\pythonProject\\PLAYER\\media\\{username}\\songs")
    thumbnail_directory = os.listdir(f"C:\\Users\\joece\\PycharmProjects\\pythonProject\\PLAYER\\media\\{username}\\songs_thumbnail")

    list = zip(songs_list,thumbnail_directory)
    data = {

        'data':list,

    }
    
    

    return render( request , 'music.html' , data )



