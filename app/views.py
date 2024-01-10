from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topic_forms(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        ETFO=Topicform(request.POST)
        if ETFO.is_valid():
            tn=ETFO.cleaned_data['topic_name']
            To=Topic.objects.get_or_create(topic_name=tn)[0]
            To.save()
            ETFO=Topic.objects.all()
            d1={'topics':ETFO}
            return HttpResponse('topic data forms is crated succesfully......!',d1)
    return render(request,'topic_forms.html',d)
def webpage_forms(request):
    EWFO=Topicform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        EWFO=Topicform(request.POST)
        if EWFO.is_valid():
            tn=EWFO.cleaned_data['topic_name']
            To=Webpage.objects.get_or_create(topic_name=tn)[0]
            To.save()
            EWFO=Topic.objects.all()
            d1={'Webpage':EWFO}
        return HttpResponse('webpage data forms is crated successfully...!',d1)
    return render(request,'webpage_forms.html',d)
def access_record_forms(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            tn=AFDO.cleaned_data['topic_name']
            To=Topic.objects.get_or_create(topic_name=tn)[0]
            To.save()
            AFDO=Topic.objects.all()
            d1={'accessrecord':AFDO}
            AFDO.save()
        return HttpResponse('accessrecord is done successfully.......!',d1)
    return render(request,'access_record_forms.html',d)



