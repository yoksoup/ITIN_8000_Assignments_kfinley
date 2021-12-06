"""
------------------------------------------------------------
Contains the urls for the clubs app list, this can be used to
import the urls for module that function is not used at the
moment and they are directly imported into {base}/urls.py
------------------------------------------------------------
"""
from django.urls import path
from .views import (
    club_create_view,
    club_detail_view,
    club_delete_view,
    club_list_view,
    club_update_view,
    
)

app_name = 'products'
urlpatterns = [
    path('', club_list_view, name='club-list'),
    path('create/', club_create_view, name='club-list'),
    path('<int:id>/', club_detail_view, name='club-detail'),
    path('<int:id>/update/', club_update_view, name='club-update'),
    path('<int:id>/delete/', club_delete_view, name='club-delete'),
]