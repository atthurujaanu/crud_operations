from django.shortcuts import render

# Create your views here.
from app.models import *

from django.db.models.functions import Length

def insert_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'insert_topic.html',d)


def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.order_by(Length('name'))
    LOW=Webpage.objects.order_by(Length('name').desc())
    LOW=Webpage.objects.exclude(topic_name='cricket')

    
    
    d={'webpage':LOW}
    return render(request,'display_webpage.html',d)

def display_accessrecords(request):
    LOA=AccessRecords.objects.all()
    LOA=AccessRecords.objects.filter(date__gt='2000-08-22')
    LOA=AccessRecords.objects.filter(date__lt='2000-08-24')
    LOA=AccessRecords.objects.filter(date__gte='2000-08-21')
    LOA=AccessRecords.objects.filter(date__lte='2000-08-21')

   

    d={'accessrecords':LOA}
    return render(request,'display_accessrecords.html',d)
