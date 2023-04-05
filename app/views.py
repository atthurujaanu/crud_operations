from django.shortcuts import render

# Create your views here.
from app.models import *
def insert_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'insert_topic.html',d)


def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    return render(request,'display_webpage.html',d)

def display_accessrecords(request):
    LOA=AccessRecords.objects.all()
    d={'accessrecords':LOA}
    return render(request,'display_accessrecords.html',d)
