"""
URL configuration for F1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('django.contrib.auth.urls')),
                  path('blog/', include('blog.urls'), name='blog'),
                  path('homepage/', include('homepage.urls'), name='homepage'),
                  path('quiz/', include('quiz.urls'), name='quiz'),
                  path('stats/', include('blog.urls'), name='stats'),
                  path('events/', include('events.urls'), name='events'),
                  path('members/', include('members.urls'), name='members'),
                  path('about/', include('aboutpage.urls'), name='about'),
                  path('stats/', include('stats.urls'), name='stats'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
