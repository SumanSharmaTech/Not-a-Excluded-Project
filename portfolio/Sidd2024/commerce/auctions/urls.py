from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("login", views.login_view, name = "login"),
    path("logout", views.logout_view, name = "logout"),
    path("register", views.register, name = "register"),
    path("CreateListing", views.CreateListing, name = "create"),
    path("active", views.active, name= "active"),
    path("listing/<int:listing_id>", views.listing, name = "listing"),
    path("add_watchlist/<int:listing_id>", views.add_watchlist, name = "add_watchlist"),
    path("watchlist", views.watchlist, name = "watchlist"),
    path("close/<int:listing_id>", views.close, name = "close"),
    path("categories", views.categories, name = "categories"),
    path("listing/<str:category>", views.category_listing, name = "category_listing"),
    path("Dashboard", views.closedlisting, name="closedlisting")
]
