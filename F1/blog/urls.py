from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import BlogMainPageView, AllPostView, SinglePostView

urlpatterns = [
    path('', BlogMainPageView.as_view(), name='blog_main_page'),
    path('posts', AllPostView.as_view(), name='posts_list'),
    path("posts/<slug:slug>", SinglePostView.as_view(),name='post-detail-page'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)