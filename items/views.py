from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item as Good


# Create your views here.
@api_view(http_method_names=['GET'])
def item_list(request):
    result = []
    goods = Good.objects.all()

    if goods:
        for each_good in goods:
            result.append({
                'id': each_good.pk,
                'title': each_good.title,
                'description': each_good.description,
                'image': each_good.image.path,
                'weight': each_good.weight,
                'price': each_good.price,
            })

    return Response({'items': result})


@api_view(http_method_names=['GET'])
def item_detail(request, pk):
    response = None
    goods = Good.objects.all()

    for each_good in goods:
        if each_good.id == pk:
            response = {
                'id': each_good.pk,
                'title': each_good.title,
                'description': each_good.description,
                'image': each_good.image.path,
                'weight': each_good.weight,
                'price': each_good.price,
            }

    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
