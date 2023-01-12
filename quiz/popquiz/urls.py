from django.urls import path
from . import views


app_name = 'popquiz'
urlpatterns = [ 
    path('popquiz/', views.IndexView.as_view(), name='index'),
    path('popquiz/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('popquiz/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('popquiz/<int:question_id>/vote/', views.vote, name='vote'),
]



