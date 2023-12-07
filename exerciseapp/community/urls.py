from django.urls import path
from .views import show_all,show_message,new_community,new_review,review_all


app_name='community'
urlpatterns = [
    path('message/<int:community_pk>/',show_message,name='showmessage'),
    path('all/',show_all,name='showall'),
    path('newcom/',new_community,name='newcommunity'),
    path('newreview/',new_review,name='newreview'),
    path('reviewall/',review_all,name='reviewall'),
    
]
