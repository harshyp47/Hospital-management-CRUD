
from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Details

import shutil
import os

"""
def index(request):

    return render(request, 'index.html')
"""

class IndexView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    

class ActionPerformed(TemplateView):

    

    def get(self, request, *args, **kwargs):
        try:
            img = request.GET['img']
            pid = request.GET['pid']
            first_name = request.GET['first_name']
            last_name = request.GET['last_name']
            building = request.GET['building']
            weight = request.GET['weight']
            gender = request.GET['gender']

            rtpcr = False

            try:

                rtpcr = request.GET['rtpcr']
                rtpcr = True

            except:
                pass

            date = request.GET['date']
            remarks = request.GET['healthremarks']
        except:
            pass

        
        
        
        if request.GET.get("add"):

            if Details.objects.filter(pid=pid).exists():
                return render(request, 'index.html',{"msg":"Record already exists!"})

            path = os.path.join("E:\SEMVI\Capstone-I\photos",str(img))
            
            shutil.copy(path, "E:/lawyer/media/pics")

            try:
                Details.objects.create(img = "pics/"+img, pid = pid, first_name = first_name, last_name = last_name, building = building, weight = weight, gender = gender, rtpcr = rtpcr, admission = date, remarks = remarks)
            except:
                return render(request, 'index.html',{"msg":"Record not saved!"})

            return render(request, 'index.html',{"msg":"Record saved successfully!"})
        
        elif request.GET.get("update"):
            
            p = Details.objects.get(pid = pid)
            p.first_name = first_name
            p.last_name = last_name
            p.img = img
            p.building = building
            p.weight = weight
            p.gender = gender
            p.rtpcr = rtpcr
            p.admission = date
            p.remarks = remarks
            p.save()




            return render(request, 'index.html',{"msg":"Record updated successfully!"})
        
        elif request.GET.get("delete"):

            p = Details.objects.get(pid = pid)
            p.delete()


            return render(request, 'index.html',{"msg":"Record deleted successfully!"})

        elif request.GET.get("show"):

            x = Details.objects.get(pid = pid)

            return render(request, 'index.html',{"msg":"Record displayed successfully!","x":x})            