from unicodedata import name
from django.urls import path 
from .import views 

urlpatterns =[
    path("", views.indexView.as_view() , name= "home"),
    path("all-post", views.allPost.as_view(), name = "allPost"),
    path("post/<slug:slug>", views.PostDetails.as_view() , name = "post-details"),
    path("profile<id>", views.porfile, name = "profile"),
    path("post-data", views.contactForm, name= "post-data"),
    path("read-later", views.ReadLaterView.as_view(), name = "read-later")
]
