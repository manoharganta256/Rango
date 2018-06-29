from django.conf.urls import url
from rango import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
    url(r'^add_category/',views.add_category,name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/',views.add_page,name="add page"),
    url(r'^register/',views.register,name="register"),
    url(r'^login/',views.user_login,name='user_login'),
    url(r'^restricted/',views.restricted,name='restricted'),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^goto/',views.track_url,name='goto'),
    url(r'^search/',views.search,name='search'),
    url(r'^like_category/', views.like_category, name='like_category'),
    url(r'^suggest_category/', views.suggest_category, name='suggest_category'),
     url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
    #url(r'^accounts/login/',views.user_login,name='auth_login')
]