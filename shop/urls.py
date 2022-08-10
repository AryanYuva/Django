from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index,name="ShopHome"),
     path("about/", views.about,name="AboutUs"),
      path("contact/", views.contact,name="contactUs"),
       path("tracker/", views.tracker,name="Trackingstatus"),
        path("search/", views.search,name="Search"),
         path("products/<int:myid>", views.productView,name="ProductView"),
          path("Checkout/", views.Checkout,name="Checkout"),
           path("", views.index,name="ShopHome"),
]      