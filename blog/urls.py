from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/',include('blog.urls', namespace='about')),
    path('',views.index, name='index'),
    path('post/', views.recent, name='post'),
    path('update/<int:id>/', views.update, name='update'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('recent/',views.recent, name='recent'),
#     path('post/', views.recent, name='post'),
#     path('about/', views.about, name='about'),
# ]