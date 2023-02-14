from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import Article


class HomepageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_articles'] = Article.objects.all().order_by('-pk')
        context['latest_articles'] = Article.objects.all()[:5]
        context['last_article'] = Article.objects.last()
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    model = User
    template_name = 'registration/login.html'
    success_url = reverse_lazy('article:home')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = '__all__'
    template_name = 'article_form.html'
