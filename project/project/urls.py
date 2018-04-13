"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from blog.views import PostListView
from blog.views import PostDetailView
from django.conf.urls.static import static
from django.conf import settings 
from blog.views import PostCreateView
from blog.views import PostUpdateView
from blog.views import PostDeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
	path('',PostListView.as_view(), name="post_list"),
	path('create/', PostCreateView.as_view(),name ="post_create"),
	path('<pk>/', PostDetailView.as_view(),name ="post_detail"),
	path('<pk>/update/', PostUpdateView.as_view(),name ="post_update"),
	path('<pk>/delete/', PostDeleteView.as_view(),name ="post_delete"),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)