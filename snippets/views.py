# tutorial 1 serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# tutorial 2 request and response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# tutorial 3 class-based Views
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics


# 더 간결해진 코드 
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# # tutorial 3 middle
# # GenericAPIView 핵심 기능 제공
# # mixins는 .list()와 .create() 기능 제공
# # 기능들을 get, post로 연결 
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# # tutorial 3 start
# class SnippetList(APIView):
#     """
#     코드 snippet의 목록을 보여주거나, 새로 snippet 생성
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class SnippetDetail(APIView):
#     """
#     snippet을 검색, 업데이트, 삭제
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# request
# request 객체는 HttpRequest 객체를 상속 받아 만들어 졌으며 
# 보다 유용한 request parsing 기능을 제공
# 핵심 기능은 request.data 속성으로 
# request.POST와 비슷하지만 Web API 작업에 더 유용
"""
request.POST  # 오직 폼 데이터를 처리하고, 오직 POST 메소드에서만 동작함
request.data  # 임의의 데이터를 처리하고, POST와 PATCH 메소드에서 동작함
"""

# response
# response 객체는  TemplateResponse 유형이며, 
# 렌더링 되지 않은 컨텐츠를 가져오고, 
# 컨텐츠 협상을 통해 클라이언트에게 반환할 올바른 컨텐츠 형식을 결정
"""
return Response(data)  # 클라이언트가 요청한 컨텐츠 유형으로 렌더링 함
"""

# status codes
"""
status 모듈 안에 있는 HTTP_400_BAD_REQUEST를 사용하여 
각각의 상태 코드를 명확하게 한다.
"""

# wrapping API views
"""
- @api_view 데코레이터는 함수 기반 뷰에서 동작한다
- APIView 클래스는 클래스 기반 뷰에서 동작한다
"""
# view에서 Request 인스턴스를 수신하는지 확인하고, 
# 컨텐츠 협상을 수행할 수 있도록 Response 객체에 context를 추가하는 등 
# 몇 가지 기능을 한다.
# 405 Method Not Allowed 응답도 제공하는데, 
# 이는 request.data에 잘못된 형식을 입력할 때 
# 일어나는 ParseError처럼 예외를 처리하는 동작 같은 것이다.


# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     # format: 응답이 더 이상 단일 콘텐츠 유형에 고정되어 있지 않다는 사실을 활용하기 위해 
#     # API 끝점에 format suffixes를 추가함.
#     # 이를 사용하면 지정된 형식을 명시적으로 참조하는 URL이 제공되며, 
#     # 이는 API가 http://example.com/api/items/4.json 과 같은 URL을 처리할 수 있음을 의미함.
#     """
#     코드 snippet의 목록을 보여주거나, 새로운 snippet 생성
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # 네이밍된 status code를 사용하고, response 의미를 전달한다.

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     # request.data는 json 요청 처리 외에도 다른 형식 요청 처리도 할 수 있다.
#     # response 객체를 반환하지만 올바른 컨텐츠 유형으로 렌더링하도록 drf가 허용한다.
#     """
# 	snippet을 검색, 업데이트, 삭제	
# 	"""
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#  튜토리얼 1 serializer
# # 이미 존재하는 snippets 목록을 보여주거나 새로운 snippets을 생성함
# @csrf_exempt
# def snippet_list(request):
#     """
#     코드 snippet의 목록을 보여주거나, 새로운 snippet 생성
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# # csrf_exempt: CSRF token을 가지고 있지 않는 사용자도 이 뷰에 POST 요청을 할 수 있도록
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     snippet을 검색, 업데이트, 삭제
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)