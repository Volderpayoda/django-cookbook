from django.urls import path
from . import views

app_name = 'cd_library'
urlpatterns = [
    # ex: /cd_library/
    path('', views.index, name='index'),
    # ex: /cd_library/5
    path('<int:pk>', views.detail, name='detail')
]
