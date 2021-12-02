from django.urls import path
from . import views
from .views import AboutView

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("about/", AboutView.as_view(), name="about"),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
