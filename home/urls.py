
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ),
    path('blog/',views.blog ),
    path('pview/<str:slug>/',views.blogview ),
    path('about/',views.about ),
    path('contect/',views.contect ),
   
]
