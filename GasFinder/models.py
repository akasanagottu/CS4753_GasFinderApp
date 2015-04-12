from django.db import models
from django import forms

tiers = (
    ("Bronze", 'Bronze Tier: $1000 per month'),
    ("Silver", 'Silver Tier: $3000 per month'),
    ("Gold", 'Gold Tier: $5000 per month'),
    ("Platinum", 'Platinum Tier: $7000 per month'),
)

class Advertiser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    tiers = models.CharField(max_length=1000, choices=tiers, default="Bronze")