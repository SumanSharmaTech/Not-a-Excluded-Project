from auctions.forms import create_form
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def active(request):
    list = Listing.objects.all()
    bid= Bid.objects.all()
    return render(request, "auctions/active.html", {
        "lists":list,
        "bidd": bid
    })

@login_required
def CreateListing(request):
    form=create_form()
    if request.method=="POST":
        list=Listing()
        forms=create_form(data = request.POST)
        if forms.is_valid():
            list.title=forms.cleaned_data["title"]
            list.description=forms.cleaned_data["description"]
            list.bid=forms.cleaned_data["bid"]
            list.image=forms.cleaned_data["image"]
            list.category=forms.cleaned_data["category"]
            list.user=request.user
            list.save()
            return render(request, "auctions/create.html",{
                "message": "Your Listing added succesfully!"
            })
        else:
            return render(request, "auctions/create.html",{
                "message": "Something went wrong please recheck the form.",
                "form": form
            })
    else:
        return render(request, "auctions/create.html",{
            "form": form
        })


def listing(request, listing_id):
    list = Listing.objects.get(id = listing_id)
    bid = Bid.objects.filter(listingkey = list)
    comm = Comment.objects.filter(listing = list)

    if request.user.is_authenticated:
        watch = Watchlist.objects.filter(listing=list, user=request.user)
    else:
        watch = "empty"

    highest_bid = list.bid
    bidd = Bid.objects.filter(listingkey = list)
    
    if bid is not None:
        
        for bidd in bid:
            if bidd.price > highest_bid:
                highest_bid = bidd.price
        
    #in case a bid or a commetn is posted
    if request.method == 'POST':
        value = request.POST.get('bid_price', None)
        user = request.user
        listing = Listing.objects.get(id = listing_id)
        comment = request.POST.get('comment', None)
        
        try:
            value = int(value)
        except:
            value = None
        
        if comment is not None:
            comm = Comment.objects.create(comment = comment, user = user, listing = listing)
            comm.save()
            
            return HttpResponseRedirect(reverse('listing', args = [listing_id]))
        
        if value is not None:
            if int(value) < highest_bid:

                return HttpResponseRedirect(reverse('listing', args = [listing_id],))
            
            bid = Bid.objects.create(price= int(value), user = user, listingkey = listing)
            bid.save()
            
            bid1 = Bid.objects.filter(listingkey = listing).exclude(price = value)
            bid1.delete()
            
            return HttpResponseRedirect(reverse('listing', args = [listing_id]))
 
    return render(request, "auctions/listing.html", {
        "listing": list,
        "highest_bid": highest_bid,
        "min_bid": (highest_bid + 1),
        "comments": comm,
        "watch": watch,
        "bid": bidd
    })
    
def categories(request):
    return render(request, "auctions/categories.html",{
        "categories":category.objects.all()
    })

def category_listing(request, category):
    cat=str(category)
    list = Listing.objects.filter(category__name=cat)
    return render(request, "auctions/category_listing.html", {
        "lists": list,
        "category":category
    })

@login_required
def add_watchlist(request, listing_id):
    
    user = request.user
    list = Listing.objects.get(id = listing_id)
    
    watch = Watchlist.objects.filter(user = user, listing = list).first()
    
    if watch is None:
        wl = Watchlist.objects.create(user = user, listing = list)
        wl.save()
        return HttpResponseRedirect(reverse("watchlist"))
    
    watch.delete()
    return HttpResponseRedirect(reverse("watchlist"))

@login_required
def watchlist(request):
    
    user = request.user
    watch = Watchlist.objects.filter(user = user)
    
    return render(request, "auctions/watchlist.html", {
        "watchlist": watch
    })

@login_required
def close(request, listing_id):
    
    list=Listing.objects.get(id = listing_id)
    win=Winner()
    bid=Bid.objects.filter(listingkey=list)
    if not bid:
        message="Deleted Listing"
    else:
        bidd=Bid.objects.get(listingkey=list)
        win.owner=request.user
        win.winner=bidd.user
        win.title=list.title
        win.image=list.image
        win.listingid=listing_id
        win.winprice=bidd.price
        win.save()

        bid.delete()
        message = "Bidding closed successfully!"
        
        if Watchlist.objects.filter(listing=list):
            watch=Watchlist.objects.filter(listing=list)
            watch.delete()
        
        if Comment.objects.filter(listing=list):
            comm=Comment.objects.filter(listing=list)
            comm.delete()
        
        winners=Winner.objects.all()

    list.delete()
    winners=Winner.objects.all()

    return render(request, "auctions/closed.html",{
        "lists": winners,
        "message": message
    })

@login_required
def closedlisting(request):

    return render(request, "auctions/closed.html",{
        "lists": Winner.objects.all()
    })