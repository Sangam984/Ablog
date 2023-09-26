from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import Post,Category,Profile
from .form import PostForm,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from .form import ProfileForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

# this is used to get the content of Category class from database to the homeView
#this code also get all the categories in the dropdown of base.html
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] =cat_menu 
        return context
    




def CategoryView(request,cats):
    cat_post = Post.objects.filter(category = cats)
    return render(request,'category.html',{'cats':cats,'cat_post':cat_post})



class ArticleView(DetailView):
    model = Post
    template_name = 'articles_detail.html'


    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView,self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_like =stuff.total_like()
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        else:
            liked = False

        context["cat_menu"] = cat_menu
        context['total_like']= total_like
        context['liked'] = liked
        return context
    

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add.html'
class AddCategoryView(CreateView):
    model=Category

    template_name = 'AddCategoryView.html'
    fields = '__all__'
    # fields = ('title','body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','author','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


# this is the code for making like system in this vlog
#get_object_or_404 is used to get the class's object 
#for eg: here through get_object_or_404 we can access Post class having id = post.id

def likeView(request, pk):
    post = get_object_or_404(Post , id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article-view',args=[str(pk)]))


class CreateProfile(UpdateView):
    template_name = "Create_prof.html"
    model = Profile
    form_class = ProfileForm







