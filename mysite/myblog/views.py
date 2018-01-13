from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from myblog.models import Post,Comment
from django.utils import timezone
from myblog.forms import PostForm, UserForm, LoginForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class index(TemplateView):
    template_name='myblog/base.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'myblog/post_detail.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostCreate(LoginRequiredMixin ,CreateView):
    login_url = '/blog/login/'
    redirect_field_name = 'myblog:post_detail'
    form_class=PostForm
    #model=Post
    template_name = 'myblog/post_create.html'

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'myblog/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user.get_username()
    post.publish(user)
    return redirect('myblog:post_detail', pk=pk)

def user_register(request):
    if request.method == 'POST':
        user_form= UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('myblog:post_list'))
    else:
        user_form = UserForm()
    return render(request,'myblog/user_register.html',{'user_form':user_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('myblog:post_list'))
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        #Nothing has been provided for username or password.
        return render(request, 'myblog/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def list(request):
    return render(request,'myblog/base.html')
