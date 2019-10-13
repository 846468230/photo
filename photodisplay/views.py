from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import CommentForm
from django.views.generic import DetailView,ListView
from .models import Comment,UserProfile
from .models import Category,Picture
# Create your views here.
from django.http import HttpResponse
class PageView(ListView):
    model = Picture
    paginate_by = 15
    context_object_name = "picture_list"
    template_name = 'photodisplay/more.html'
    def get_queryset(self,**kwargs):
        """重写get_queryset方法，根据标签过滤当前数据"""
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        queryset = queryset.filter(category__id=category_id).exclude(status=Picture.STATUS_DELETE)
        return queryset

class comment():
    def get(self,request,*args,**kwargs):
        comment_form = CommentForm()
        context = {
            'comment_form':comment_form,
        }
        return self.render_to_response(context)

class IndexView(ListView):
    #model = Category
    queryset = Category.objects.exclude(status = Category.STATUS_DELETE)
    context_object_name = 'category_list' #模板中获取的变量名称 不设置则需要使用object_list变量
    template_name = 'photodisplay/index.html'
    

class AboutView(TemplateView):
    context_object_name = 'user_list' #模板中获取的变量名称 不设置则需要使用object_list变量
    template_name = 'photodisplay/about.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'author':UserProfile.author,
        })
        return context

def index(request):
    return  HttpResponse("Hellow world you are at the photodisplay index")

class HomeView(TemplateView):
    template_name = 'photodisplay/home.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'author':UserProfile.author,
        })
        return context

class CommentFormView(TemplateView):
    model = Comment
    template_name = 'photodisplay/comment.html'
    def get(self,request,*args,**kwargs):
        picture_id = self.kwargs.get('picture_id')
        comment_form = CommentForm()
        context = {
            'comment_form':comment_form,
            'target':picture_id,
        }
        return self.render_to_response(context)

class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = "photodisplay/result.html"
    def post(self,request,*args,**kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get("target")
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
        else:
            succeed = False
        context = {
            'succeed':succeed,
            'form':comment_form,
            'target':target,
        }
        return self.render_to_response(context)
