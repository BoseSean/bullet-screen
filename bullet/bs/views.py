from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bul, Color
from .serializers import BulSerializer
# Create your views here.

def bs_create(request):
    pass
def bs_show(request):
    context ={}
    return render(request,"base.html",context)

class bs_api(APIView):
    def get(self,request):
        not_shown_buls = Bul.objects.all()
        serializer = BulSerializer(not_shown_buls, many=True)
        return Response(serializer.data)