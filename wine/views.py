from django.shortcuts import render
from django.http import JsonResponse
from .models import Winetable
from django.core import serializers
from django.http import HttpResponse

def normFun(x):
    if x == None:
            return 1000000000000
    else:
            return x 

# GET Req
# Param: index
def getWines(req):
    if req.method == 'GET':
        print("hello1")
        idx = int(req.GET.get('index', '1'))
        filtCountry = req.GET.get('country', '')
        filtProvince = req.GET.get('province', '')
        filtRegion = req.GET.get('region', '')
        isPriceSorted = req.GET.get('priceSorted', 'False')
        isPointSorted = req.GET.get('pointSort', 'False')
        if isPriceSorted == "false":
            isPriceSorted = False
        else:
            isPriceSorted = True
        if isPointSorted == "false":
            isPointSorted = False
        else:
            isPointSorted = True

        print(isPriceSorted)
        print("kapa:"+filtCountry)
        wines = Winetable.objects.all()
        if filtCountry != '':
            wines = wines.filter(country=filtCountry)
        if filtProvince != '':
            wines = wines.filter(province=filtProvince)
        if filtRegion != '':
            wines = wines.filter(region_1=filtRegion)
        if isPriceSorted:
            wines = wines.order_by('price').filter(price__isnull=False)

        wines = wines[idx:idx+10]
        data = serializers.serialize('json', wines)
        return HttpResponse(data, content_type='application/json')