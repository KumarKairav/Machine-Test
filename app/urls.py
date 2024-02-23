from django.urls import path
from .views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView, \
                   ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView
from app import views

urlpatterns = [
    path('',views.custom_index_view, name='index'),
    path('api/clients/', ClientListCreateAPIView.as_view(), name='client-list'),
    path('api/clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-detail'),
    path('api/projects/', ProjectListCreateAPIView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
]