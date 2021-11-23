from django.urls import path
from snippets import views

# 뷰에서 만든 함수를 url에 매핑(연결)

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]