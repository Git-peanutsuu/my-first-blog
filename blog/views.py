from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import Postform
from django.shortcuts import redirect

# Create your views here.
# view.py bridge HTML file viwe between DB and templates
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
def post_detail(request, pk:int):
    # Post.objects.get(pk=pk) is not suggested. code below is better.
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method =="POST":
        form = Postform(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Postform(request.POST, instance=post) #開き保存する場合
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform(instance=post) #ただ開くだけ
    return render(request, 'blog/post_edit.html', {'form': form})