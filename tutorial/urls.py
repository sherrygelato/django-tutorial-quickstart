"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

# viewsets를 사용하기 때문에 router 클래스에 viewsets를 등록하면 
# api에 대한 url conf를 자동으로 생성할 수 있다.
# 즉, api url에 대한 더 많은 제어가 필요한 경우라면,
# regular class-based views 사용과 동시에 url conf를 명시적으로 작성한다.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# 자동 URL 라우팅을 사용하여 API를 연결한다.
# 또한 검색 가능한 API에 대한 로그인 URL을 포함한다.
urlpatterns = [
    # path('', include(router.urls)),
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]