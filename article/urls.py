from django.urls import path
from article.views import HomepageView, ArticleListView, ArticleDetailView, UserRegisterView, ArticleCreateView


app_name = "article"

urlpatterns = [
 path('', HomepageView.as_view(), name="home"),
 path('all-articles/', ArticleListView.as_view(), name="all_articles"),
 path('article/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
 path('accounts/register', UserRegisterView.as_view(), name="register"),
 path('create-article/', ArticleCreateView.as_view(), name="article_create")
]
