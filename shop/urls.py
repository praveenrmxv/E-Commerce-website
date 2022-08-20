from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="Shop Home"),
    path('about/<int:id>', views.about, name="About Us"),
    path('contact1/', views.contact1, name="contact1"),
    path('about/', views.about, name="About Us"),
    path('tracker/', views.tracker, name="tracker"),
    path('productView/<int:myid>', views.productView, name="productView"),
    path('search/>', views.search, name="search"),
    path('checkout/', views.checkout, name="Checkout"),

]