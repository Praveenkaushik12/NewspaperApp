from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy 
from .models import Article
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView

# Create your views here.

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model=Article
    template_name='article_new.html'
    fields=('title','body',)
    login_url = 'login'
    
    
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ArticleListView(LoginRequiredMixin,ListView):
    model=Article
    template_name='article_list.html'
    context_object_name='articles_list'
    login_url = 'login'
    
class ArticleDetailView(LoginRequiredMixin,DetailView):
    model=Article
    template_name='article_details.html'
    # login_url = 'login'
    
class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Article
    fields = ('title', 'body',)
    template_name='article_edit.html'
    login_url = 'login'
    # success_url=reverse_lazy('article_details')
    
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user
    
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Article
    template_name='article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user
    
    
