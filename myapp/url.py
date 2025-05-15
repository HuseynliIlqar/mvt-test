from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('why_us/', views.why_us, name='why_us'),
    path('trainer/', views.trainer, name='trainer'),
    path('contact/', views.contact, name='contact'),
    path('blog_page/', views.blog_page, name='blog_page'),
    path('success/', views.success_view, name='success'),
    path('shop/', views.shop, name='shop'),
    path('news/', views.news, name='news'),
]