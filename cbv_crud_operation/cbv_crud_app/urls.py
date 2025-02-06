from django.urls import path
from cbv_crud_app import views
urlpatterns = [
    path('',views.hello,name='hello'),
]
