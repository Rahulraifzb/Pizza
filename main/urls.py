from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverview, name="home"),
    path('pizza-list/', views.pizzaList, name="pizza-list"),
    path('pizza-detail/<str:pk>/', views.pizzaDetail, name="pizza-detail"),
    path('pizza-create/', views.pizzaCreate, name="pizza-create"),
    path('pizza-update/<str:pk>/', views.pizzaUpdate, name='pizza-update'),
    path('pizza-delete/<str:pk>/', views.pizzaDelete, name='pizza-delete'),
]
