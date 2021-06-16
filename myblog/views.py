from myblog.forms import SimpleForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Feedback, Post
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView, FormView
from django.urls import reverse
from django.contrib.auth.models import User



# Create your views here.
def home(request):
    #dictionary with initial data
    #with field name as keys
    context= {}
    #add dictionary during initialization
    context["objects"]= Post.objects.all()[:4]
    return render(request, "home.html", context)

class MyView(View):
      def get(self, request):
          return HttpResponse("My first class based views")

class CategoryList(ListView):
    model=Category

class CategoryDetail(DetailView):
    model=Category

class CategoryCreate(CreateView):
    model=Category
    #specify the fields to be displayed
    fields=['name']
    #function to redirect users
    def get_success_url(self):
        return reverse('category_list')

class CategoryUpdate(UpdateView):
    model=Category
    fields=['name']
    success_url="/categories"

class CategoryDelete(DeleteView):
    model=Category

    success_url="/categories"

class SimpleFormView(FormView):

    #specify the form you want to use
    form_class= SimpleForm

    #specify name of template
    template_name="simpleform.html"

    #specify success url
    success_url="/categories"

def welcome(request):

    context = {}

    context = User.objects.all()

        # context={
        #     'name':'Jazzy','Lopha'
        #     'email': 'lisaoloo31@gmail.com','Travels'
        # }
    return render(request, "welcome.html", context)

def posts (request):
    context={} 


    return render (request,'myblog/post_list.html', context)

class PostDetail(DetailView):
    model= Post

class FeedbackCreate(CreateView):
    model= Feedback
    fields= {'user_name', 'message'}
    
    def get_success_url(self):
        return reverse('home.html')

class PostCreate(CreateView):
    model= Post
    fields= {'title', 'post', 'category_id'}
    
    def get_success_url(self):
            return reverse('home.html')





