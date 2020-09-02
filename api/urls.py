from django.urls import path
from .views import Athletes, ListAthletesView
from . import views

urlpatterns = [
    path('athletes/', Athletes.as_view(), name="athletes"),
    path('athletes/<int:id>/', Athletes.as_view(), name="athletes"),
    path('athletes_listview/', ListAthletesView.as_view(), name="listview"),
    path('athletes_listview/<int:id>', ListAthletesView.as_view(), name="listview"),
    path('athletes_html/', views.index, name="webpage")

]

