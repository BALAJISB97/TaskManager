from django.shortcuts import render,HttpResponse,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.models import Task
from webapp.serializers import TaskSerializer
from django.contrib.auth.models import User,auth,AnonymousUser

class TaskList(APIView):
    def get(self,request):
        obj = Task.objects.filter(user=request.user).order_by('-TaskAddedTime')
        serializedObj = TaskSerializer(obj,many=True)
        return Response(serializedObj.data) 
    
    def post(self,request):
        sobj = TaskSerializer(data=request.data,many=False)
        print(sobj)
        if sobj.is_valid():
            print('Not here!! (:')
            sobj.save()
            return Response(sobj.data,status=status.HTTP_201_CREATED)
        return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
class TaskUpdateDelete(APIView):

    def getObject(self,pk):
        try:
            obj = Task.objects.get(pk=pk)
            return obj
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk):
        sobj = self.getObject(pk)
        nsobj = TaskSerializer(sobj)
        print(nsobj.data,nsobj)
        return Response(nsobj.data)
    
    def put(self,request,pk):
        sobj = self.getObject(pk)
        sobj = TaskSerializer(sobj,data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_201_CREATED)
        return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        print('delete called!')
        obj = self.getObject(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class checkLoginStatus(APIView):
    def get(self,request):
        user = {'isLoggedIn':False}
        if request.user!=AnonymousUser():
            user['isLoggedIn']=True
            user['userid']=request.user.id
            print(request.user.id)
        return Response(data=user)


        