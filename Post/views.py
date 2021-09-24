from django.shortcuts import render


# Create your views here.


from django.views.generic import ListView,DetailView,CreateView
from . models import Post 
# //Post -this is modelname
from .forms import PostCreateForm

class HomeView(ListView):
    queryset = Post.objects.order_by("-Created_on")
    # //'objects' is given bcz class is used in model

    template_name = "home.html"

class PostDetailsView(DetailView):
    model = Post
    template_name = "postdetails.html"

class CreatePostView(CreateView):
    model=Post
    form_class= PostCreateForm
    template_name='createpost.html'