from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponseBadRequest
from django.conf import settings
import os


class Athletes(APIView):
    """ API Endpoint for other applications """

    def get(self, request):

        # Open and read json file
        json_file = open(os.path.join(settings.BASE_DIR, 'static/players.json'))
        json_data = json.load(json_file)
        json_file.close()

        result = {"athlete": {}}

        # If an ID or list of IDs was specified
        if len(request.GET.getlist("id")) != 0:
            num_athletes = len(json_data["athlete"])

            for ID in request.GET.getlist("id"):
                if 0 < int(ID) <= num_athletes:
                    # Append to results
                    result["athlete"][ID] = json_data["athlete"][ID]

            # If at least 1 result
            if len(result["athlete"]) > 0:
                return JsonResponse(result, safe=True, status=200)
            else:
                return HttpResponseBadRequest("Invalid ID")
        # If no ID specified then return all athletes
        elif len(request.GET.keys()) == 0:
            return JsonResponse(json_data, safe=True, status=200)
        # If other parameters specified then return error message
        else:
            return HttpResponseBadRequest("Invalid Parameters")


class ListAthletesView(generics.ListAPIView):
    """ User friendly - Django Rest Framework API list view """

    def get(self, request):

        # Open and read json file
        json_file = open(os.path.join(settings.BASE_DIR, 'static/players.json'))
        json_data = json.load(json_file)
        json_file.close()

        result = {"athlete": {}}

        # If an ID or list of IDs was specified
        if len(request.GET.getlist("id")) != 0:
            num_athletes = len(json_data["athlete"])

            for ID in request.GET.getlist("id"):
                if 0 < int(ID) <= num_athletes:
                    # Append to results
                    result["athlete"][ID] = json_data["athlete"][ID]

            # If at least 1 result
            if len(result["athlete"]) > 0:
                return Response(result, status=200)
            else:
                return Response("Invalid ID", status=400)
        # If no ID specified then return all athletes
        elif len(request.GET.keys()) == 0:
            return JsonResponse(json_data, safe=True, status=200)
        else:
            return HttpResponseBadRequest("Invalid Parameters")


def index(request):
    return render(request, "index.html")
