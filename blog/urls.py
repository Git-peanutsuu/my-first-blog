from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('comment/<int:pk>/approve/<int:id>', views.comment_approve, name='comment_approve'),
    # path('comment/<int:pk>/remove/<int:id>', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),#ブラウザでpost.pkが渡され、int:pkでこのurls.pyが起点となって、pkをviews.py渡す
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<pk>/comment/', views.add_comment_to_post, name ='add_comment_to_post'),
    path('post/new/', views.post_new, name = 'post_new')
]