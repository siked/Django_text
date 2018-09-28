
from django.urls import path
from . import view

urlpatterns = [
    path('', view.hello),
    path('world/', view.world),
    path('get/', view.search_get),
    path('post/', view.search_post),
]