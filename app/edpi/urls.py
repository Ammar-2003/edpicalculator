from django.urls import path
from . import views

urlpatterns = [
    path('', views.edpi_calculator , name='edpi_calculator' ),
    path('what-is-edpi-in-gaming/', views.what_is_edpi, name='what_is_edpi' ),
]
