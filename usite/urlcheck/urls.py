from . import views
from django.urls import path
urlpatterns = [
      path("", views.URLListView.as_view(), name="url_list"),
      path("login", views.UsiteLoginView.as_view(), name="login"),
      path("add", views.URLCreateView.as_view(), name='add'),
      path("<int:pk>/delete", views.URLDeleteView.as_view(), name='url_confirm_delete'),
]
