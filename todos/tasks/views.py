from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# * Import the TASK serializer
from .serializers import TaskSerializer
from .models import Task


# Create your views here.


@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'list': '/task-list/',
        'detail view':  '/task-detail/<str:pk>/',
        'create': '/task-create/',
        'update': '/task-update/<str:pk>/',
        'delete': '/task-delete/<str:pk>/'
    }


    return Response(api_urls)

# * VIEW ALL TASKS
@api_view(['GET'])
def tasksList(request):

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# * VIEW A SINGLE TASK
@api_view(['GET'])
def detailView(request, pk):

    try:
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return HttpResponse(status=404)


# * CREATE A TASK
@api_view(['POST'])
def createTask(request):

    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


# * DELETE A SINGLE TASK
@api_view(['DELETE'])
def taskDelete(request, pk):

    try:
        taskToDelete = Task.objects.get(pk=pk)
        taskToDelete.delete()
        return HttpResponse(status=204)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

# * UPDATE A TASK
@api_view(['PUT'])
def updateTask(request, pk):

    try:
        tasktToUpdate = Task.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = TaskSerializer(tasktToUpdate, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

# ! CLASS EXAMPLE

# class TaskDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             return HttpResponse(status=404)

#     def get(self, request, pk, format=None):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task, many=False)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         taskToUpdate = self.get_object(pk)
#         serializer = TaskSerializer(taskToUpdate, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error_messages, status=400)

    
    


    

