from django.conf.urls import url

from fira import views


urlpatterns = [
    url(
        r'^$',
        views.FiraCreateView.as_view(),
        name='create',
    ),
]
