from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

# tutorial 1,2
# # 뷰에서 만든 함수를 url에 매핑(연결)
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# 반드시 추가할 필요는 없지만, 
# 특정 형식을 참조하는 간단하고 깔끔한 방법을 제공하는 것
urlpatterns = format_suffix_patterns(urlpatterns)