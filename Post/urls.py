from django.urls import path, include
from . views import HomeView, PostDetailsView, CreatePostView

urlpatterns = [
   path('', HomeView.as_view(), name= "home"),
#    //as_view is used bcz CLASS is used

   path('article/<int:pk>',PostDetailsView.as_view() ,name ="postdetails_path"),
   path('create post/',CreatePostView.as_view() ,name ="createpost_path")

]