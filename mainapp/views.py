from django.db import models
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        #Likes:
        like_object = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = like_object.total_likes()
        liked = False
        if like_object.likes.filter(id=self.request.user.id).exists():
            liked = True
        #Context Dict:
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked']= liked
        return context

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = EditForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm
    succes_url = reverse_lazy('')
    ordering = ["-date_added"]

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

def CategoryView(request, category):
    category_posts = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'category_view.html', {
        'category':category.title().replace('-', ' '),
        'category_posts':category_posts
    } )

def DateView(request, desc):
    if desc=='desc':
        date_posts = Post.objects.order_by('-post_date')
    elif desc=='asc':
        date_posts = Post.objects.order_by('post_date')
    elif desc=='title-desc':
        date_posts = Post.objects.order_by('-title')
    elif desc=='title-asc':
        date_posts = Post.objects.order_by('title')
    elif desc=='author-desc':
        date_posts = Post.objects.order_by('-author')
    elif desc=='author-asc':
        date_posts = Post.objects.order_by('author')
    elif desc=='all':
        date_posts = Post.objects.order_by('title')
    elif desc=='likes':
        date_posts = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')




    return render(request, 'filtered_posts.html',{
        'date_posts': date_posts
    })

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))



'''podria cambiar DateView por un filtro llamado SortView(request,*args,**kwargs)
el cual tome el argumento y lo pase como query dentro de order_by('algo')
para eso tambien tendremos que modificar la url a path/<str:algo>'''