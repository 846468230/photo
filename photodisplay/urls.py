from django.urls import path
from . import views
from .views import CommentFormView
from .views import CommentView,PageView,IndexView,AboutView,HomeView
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('photos/',IndexView.as_view(),name="index"),
    path('more/<int:category_id>',PageView.as_view(),name="more"),
    path('comment/<int:picture_id>',CommentFormView.as_view(),name="comment"),
    path('comment_result/',CommentView.as_view(),name="comment_result"),
    path('about/',AboutView.as_view(),name="about"),
]