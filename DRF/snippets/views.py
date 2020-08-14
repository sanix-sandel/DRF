from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method=='GET':
        snippets=Snippet.objects.all()
        serializer=SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)        


"""
we want to be able to POST to this view from clients that 
won't have a CSRF token we need to mark the view as csrf_exempt
"""

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snippet=Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=404)

    if request.method=='GET':
        serializer=SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method=='PUT':
        
        serializer=SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method=='DELETE':
        snippet.delete()
        return Response(status=204)               
