from django.urls import path 

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('result', views.result),
    path('display_results', views.display_results),
]