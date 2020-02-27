from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.signup, name='signup'),
    url(r'^account/', include('django.contrib.auth.urls')),
    # url(r'^logout/$', views.logout, {"next_page": '/'}), 
    url(r'^profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    url(r'^profile/<username>', views.profile, name='profile'),
    url(r'^all-hoods/',views.neighbourhoods,name='hood'),
    url(r'^new-hood/', views.create_neighbourhood, name='new-hood'),
    url(r'^join_hood/(\d+)', views.join_neighbourhood, name='join-hood'),
    url(r'^leave_hood/(\d+)', views.leave_neighbourhood, name='leave-hood'),
    url(r'^single_hood/(\d+)', views.single_neighbourhood, name='single-hood'),
    url(r'^(\d+)/new-post', views.create_post, name='post'),
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)