from django.shortcuts import render, redirect
from .models import Post, Blog
from .forms import PostForm

def blogs(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts, 'form': form}
    return render(request, 'blog.html', context)

def blog_list(request):
    blogs = Blog.objects.all()
    query = request.GET.get('q')
    if query:
        blogs = blogs.filter(title__icontains=query)
    return render(request, 'blog.html', {'blogs': blogs})