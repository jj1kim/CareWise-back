from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Search
import json

class CarelabelSearchView(APIView):
  def get(self, request):
    data = json.loads(request.body)
    imgurl = data['imgurl']
    imgkey = data['imgkey']
    contents = {"data": "hello world",
                "imgurl": f"{imgurl}",
                "imgkey": f"{imgkey}"}
    return Response(contents, status=status.HTTP_200_OK)