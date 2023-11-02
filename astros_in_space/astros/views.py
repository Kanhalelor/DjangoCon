from django.conf import settings
from django.shortcuts import render
from django.template import loader
from django.templatetags.static import static
import requests
import os

# Create your views here.

def astronauts(request):
    """Get austronaut data using open-notify API"""
    # get all static images from the static dir
    image_folder = "images"
    image_files = os.listdir(os.path.join('static', image_folder))
    
    # Generate image URLs using the static template tag
    image_urls = [static(os.path.join(image_folder, image)) for image in image_files]

    # experimenting
    # image_files = ["image1.jpg", "image2.jpg", "image3.jpg"]
    
    URL = "http://api.open-notify.org/astros.json"
    resp = requests.get(url=URL)
    data = resp.json()
    message = data["message"]
    number = data["number"]
    people = data["people"]
    people.sort(key=lambda x: x['name'].split()[-1])

    context = {
        "message": message,
        "number": number,
        "people_with_images": zip(people, image_urls),
    }

    return render(request, "astros/index.html", context)