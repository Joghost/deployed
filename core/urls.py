from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('profiles',views.profiles, name='profiles'),
    path('payment', views.payment, name='payment'),
    path('report-post', views.report_post, name='report-post'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('comment', views.comments, name='comment'),
    path('product-search', views.search_product, name='product-search'),
    

]