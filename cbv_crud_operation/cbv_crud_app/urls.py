from django.urls import path
from cbv_crud_app import views

urlpatterns = [
    path('',views.HomeTemplate.as_view(),name='home'),
    path('list_data/',views.TeamDetailListView.as_view(),name='list_data'),
    path('create_data/',views.TeamDetailCreateView.as_view(),name='create_data'),
    path('detail_data/<int:pk>/',views.TeamDetailDetailView.as_view(),name='detail_data'),
    path('update_data/<int:pk>/',views.TeamDetailUpdateView.as_view(),name='update_data'),
    path('delete_data/<int:pk>/',views.TeamDetailDeleteView.as_view(),name='delete_data'),
]
