from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restapi.models import Configuration, Usrs, Grp
from restapi.serializer import ConfigurationSerializer, UsrsSerializer, GrpSerializer
# Create your views here.

class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer


class UsrsViewSet(viewsets.ModelViewSet):
    queryset = Usrs.objects.all()
    serializer_class = UsrsSerializer


class NoGrpUsrsViewSet(viewsets.ModelViewSet):
    queryset = Usrs.objects.all()
    serializer_class = UsrsSerializer

    def list(self, request, *args, **kwargs):
        queryset = Usrs.objects.all()
        queryset = queryset.filter(grp_id__isnull=True)
        serializer = UsrsSerializer(queryset, many=True)
        return Response(serializer.data)

class MyGrpViewSet(viewsets.ModelViewSet):
    queryset = Usrs.objects.all()
    serializer_class = GrpSerializer

    def list(self, request, *args, **kwargs):
        queryset = Usrs.objects.all()
        my_param = request.GET.get('my_param')
        print(str(request))
        params=request.query_params
        print(str(params))
        grpid = request.query_params.get('grp_id')
        print(grpid)
        queryset = queryset.filter(grp_id=grpid)
        serializer = UsrsSerializer(queryset, many=True)
        return Response(serializer.data)

class GrpViewSet(viewsets.ModelViewSet):
    queryset = Grp.objects.all()
    serializer_class = GrpSerializer


