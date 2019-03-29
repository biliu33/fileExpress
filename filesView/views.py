# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from tempUtil import transListToPath, getDefaultPath
from django.http import StreamingHttpResponse
# Create your views here.


def generateLink(locationList, fileName):
    locationList = [_ for _ in locationList if _]
    return locationList[-1] + "/" + fileName


def calFileName(absFilePath):
    fileName = ([_ for _ in absFilePath.split("/") if _])[-1]
    return fileName


def generateFileDownloadLink(locationList, fileName):
    locationList = [_ for _ in locationList if _]
    return locationList[-1] + "/" + fileName


def index(request):
    currentLocation = request.path.split("/")[2:]
    if currentLocation[0]:
        realLocation = transListToPath(currentLocation)
    else:
        currentLocation = [getDefaultPath()]
        realLocation = transListToPath([getDefaultPath()])
    if os.path.exists(realLocation) and os.path.isdir(realLocation):
        files = os.listdir(realLocation)
        infos = list()
        for file in files:
            infos.append({"fileName": file,
                          "linkUrl": generateLink(currentLocation, file),
                          "absPath": os.path.join(realLocation, file)})
        directoryInfos = [partInfo for partInfo in infos
                          if os.path.isdir(partInfo["absPath"])]
        fileInfos = [partInfo for partInfo in infos
                     if not os.path.isdir(partInfo["absPath"])]
        return render(request, "filesView.html",
                      {"directoryInfos": directoryInfos,
                       "fileInfos": fileInfos})
    else:
        return render(request, "error.html")


def downloadFile(request):
    currentLocation = request.path.split("/")[2:]
    if currentLocation[0]:
        realLocation = transListToPath(currentLocation)
    else:
        currentLocation = [getDefaultPath()]
        realLocation = transListToPath([getDefaultPath()])
    file = open(realLocation, "rb")
    response = StreamingHttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    # print "filename", calFileName(realLocation)
    response['Content-Disposition'] = 'attachment;filename="{fileName}"'\
        .format(fileName=calFileName(realLocation))
    return response
