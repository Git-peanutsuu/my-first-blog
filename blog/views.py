from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import Postform, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
# view.py bridge HTML file viwe between DB and templates
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
def post_detail(request, pk:int):
    # Post.objects.get(pk=pk) is not suggested. code below is better.
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def add_comment_to_post(request, pk:int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk) #post.pkであるひつよう
    else:
        form = CommentForm(request.GET)
    return render(request, 'blog/add_comment_to_post.html', {'form': form,'post':post})
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

@login_required
def post_new(request):
    if request.method =="POST":
        form = Postform(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform()
    return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Postform(request.POST, instance=post) #開き保存する場合
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform(instance=post) #ただ開くだけ
    return render(request, 'blog/post_edit.html', {'form': form})

# @login_required
# # わからない！！
# def comment_approve(request,pk, id):
#     post = get_object_or_404(Post, pk = pk)
#     comment = get_object_or_404(Comment, id=id)
#     # ここでエラー
#     # objectの取得方法はあっているんか。
#     # そもそもデータベースにこのデータが記録されているのん
#     print('def comment_approve')
#     comment.approve()
#     return redirect('post_detail', pk=post.pk, id=comment.pk)

# @login_required
# # わからない！！
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.delete()
#     return redirect('post_detail', pk=comment.post.pk)