from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status
from .models import Emp
from .serializers import EmpSerializer

class EmpView(APIView):
    def get(self,request):
        emps = Emp.objects.all()
        serializer = EmpSerializer(emps , many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = EmpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'new object is added to Database'})
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


class EmpDetails(APIView):

    def get(self,request,pk):
        e = Emp.objects.get(empid=pk)
        serializer = EmpSerializer(e)
        return Response(serializer.data)

    def put(self,request,pk):
        e = Emp.objects.get(empid=pk)
        serializer = EmpSerializer(e,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'objects is successfully updated'})

        else:
            return Response({'message' : 'Record is not updated succefully'})

    def delete(self,request,pk):
        e = Emp.objects.get(empid=pk)
        e.delete()
        return Response({'message' : 'Record deleted succefully'})

