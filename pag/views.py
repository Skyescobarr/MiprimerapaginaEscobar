# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Comment 
from .forms import PostForm, CategoryForm, CommentForm, PostSearchForm
from django.db.models import Q

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'pag/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all() # type: ignore
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'pag/post_detail.html', {'post': post, 'comments': comments, 'comment_form': form})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # Si quieres que el autor sea el usuario logueado, descomenta la siguiente línea:
            # post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'pag/post_form.html', {'form': form, 'form_title': 'Crear Nuevo Post'})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('post_list')
    else:
        form = CategoryForm()
    return render(request, 'pag/category_form.html', {'form': form, 'form_title': 'Crear Nueva Categoría'})

def post_search(request):
    form = PostSearchForm()
    results = []
    query = None
    if 'query' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
    return render(request, 'pag/search_results.html', {'form': form, 'results': results, 'query': query})

