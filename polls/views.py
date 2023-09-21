from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import KorxonaSerializer
from rest_framework.response import Response
from .models import Korxona
from django.shortcuts import get_object_or_404


# Create your views here.


    

class AllSee(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":


            print(self.request.user.roles)
            x = Korxona.objects.filter(status=True)
            serializer=KorxonaSerializer(x, many=True)
            return Response(serializer.data)
        
        return Response({'msg':'Please log in'})
    
class PatchStatus(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":


            if request.user.roles == 3:
                x= get_object_or_404(Korxona, id=kwargs['forid'])
                serializer=KorxonaSerializer(x, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            
        return Response("Only admin can change")
    

class YaratishView(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.roles == 2:
                serialzier = KorxonaSerializer(data=request.data)
                if serialzier.is_valid():
                    serialzier.save()
                    return Response(serialzier.data)
                return Response(serialzier.errors)
        return Response({"msg":"only staff members can add"})