from rest_framework import serializers

from todos.constants import STATUS_CHOICES


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

class TodoSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=200, read_only=True)
    name = serializers.CharField(max_length=200)
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    due_date = serializers.DateTimeField()
