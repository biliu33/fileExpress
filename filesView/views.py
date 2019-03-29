# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import os
from tempUtil import transListToPath

# Create your views here.


def generateLink(locationList, fileName):
    locationList = [_ for _ in locationList if _]
    return locationList[-1] + "/" + fileName


def index(request):
    print "request path", request.path
    currentLocation = request.path.split("/")[2:]
    if currentLocation[0]:
        realLocation = transListToPath(currentLocation)
    else:
        realLocation = "C:/"
    print realLocation
    if os.path.exists(realLocation) and os.path.isdir(realLocation):
        files = os.listdir(realLocation)
        infos = list()
        for file in files:
            infos.append({"fileName": file, "linkUrl": generateLink(currentLocation, file),
                          "absPath": os.path.join(realLocation, file)})
        directoryInfos = [partInfo for partInfo in infos if os.path.isdir(partInfo["absPath"])]
        fileInfos = [partInfo for partInfo in infos if not os.path.isdir(partInfo["absPath"])]
        return render(request, "filesView.html", {"directoryInfos": directoryInfos, "fileInfos": fileInfos})
    else:
        return render(request, "error.html")
