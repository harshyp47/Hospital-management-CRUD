from django.urls import path
from . import views
from crud.views import IndexView, ActionPerformed

urlpatterns = [
    #path('', views.index),

    path('', IndexView.as_view()),
    path('actionperformed', ActionPerformed.as_view())
    

    
]