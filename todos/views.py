from django.shortcuts import render
from rest_framework.exceptions import NotFound

from todos.firebase_client import FirebaseClient
from todos.serializers import TodoSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

'''
http://127.0.0.1:8000/api/v1/todos/

GET Single todo - http://127.0.0.1:8000/api/v1/todos/5i3KhTB8EYh1vZBqtd7v/

Sample json Format
{
    "name": "sdd",
    "status": "Pending",
    "due_date": "2022-03-22T22:33:00Z"
}

'''

class TodoViewSet(viewsets.ViewSet):
    client = FirebaseClient()

    def create(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.create(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def list(self, request):
        todos = self.client.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todo = self.client.get_by_id(pk)

        if todo:
            serializer = TodoSerializer(todo)
            return Response(serializer.data)

        raise NotFound(detail="Todo Not Found", code=404)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.client.delete_by_id(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.update(pk, serializer.data)

        return Response(serializer.data)


import requests

def display_todos(request):

    todos = requests.get('http://127.0.0.1:8000/api/v1/todos/')
    print(todos.json(),'todossssssss')
    context = {'todos':todos.json()}
    return render(request,'index.html',context=context)

