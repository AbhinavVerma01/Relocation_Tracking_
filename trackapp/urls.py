from django.urls import path
from .views import request_tracker,post_tracker


urlpatterns = [
    # path('tracker/', trackerView.as_view(),),       #for classss--------------
    # path('tracker/<int:pk>/', trackerView.as_view(), ),  
    path('tracker/', post_tracker),
    path('tracker/<int:pk>/', request_tracker, ),
    
]
