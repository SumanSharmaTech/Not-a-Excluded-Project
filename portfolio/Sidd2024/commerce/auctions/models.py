from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
from django.core.validators import MinValueValidator

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length = 64)
    description = models.TextField()
    bid = models.FloatField(validators = [MinValueValidator(1)])
    image = models.URLField(blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "owner")
    category = models.ForeignKey(null=True, blank=True, on_delete=models.CASCADE,to='category')
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return (f"{self.id} {self.title}  ${self.bid} {self.category}")
    
class Bid(models.Model):
    price = models.FloatField(validators = [MinValueValidator(1)])
    listingkey = models.ForeignKey(Listing, verbose_name = "listing", on_delete=models.CASCADE,related_name='cost',null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    

class category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, blank = False)

class Winner(models.Model):
    owner=models.CharField(max_length=64)
    winner=models.CharField(max_length=64)
    listingid=models.IntegerField()
    title=models.CharField(max_length=64)
    image=models.URLField()
    winprice=models.FloatField()

    def __str__(self):
        return f"{self.title} won by {self.winner} for ${self.winprice}"