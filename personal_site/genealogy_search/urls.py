from django.urls import path
from . import views

urlpatterns = [
    path('', views.genealogy, name='genealogy'),
    path('search/', views.search, name='search'),
    path('search/results/', views.results, name='search_results'),
    path('search/record/<int:collection_id>/<int:record_id>', views.record, name='record'),
    path('trees/<slug:slug>', views.trees, name='trees'),
]
