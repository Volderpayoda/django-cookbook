from django.urls import path
from . import views

app_name = 'cd_library'
urlpatterns = [
    # ex: /cd_library/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /cd_library/5
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    # ex: /cd_library/create
    path('create/', views.CreateView.as_view(), name="create"),
    # ex: /cd_library/5/delete
    path('<int:pk>/delete', views.DeleteView.as_view(), name="delete")
]
