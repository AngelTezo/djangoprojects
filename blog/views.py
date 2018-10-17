from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .form import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def listar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/listar.html', {'post': post})

def agregar(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('listar', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/agregar.html', {'form': form})



def editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('listar', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/agregar.html', {'form': form})

def borrador(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/borrador.html', {'posts': posts})

def publicar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('listar', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()         

def eliminar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('list')
# Create your views here.
