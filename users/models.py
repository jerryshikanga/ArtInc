from django.db import models
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from bids.models import Bid

class CustomUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    website = models.URLField(blank=True)
    telephone = models.CharField(max_length=30, blank=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    picture = models.ImageField(upload_to='uploads/customuser/profile/', blank=True)

    def deposit(self, amount):
        self.balance += amount
        self.save()
        return True

    def withdraw(self, amount):
        if self.balance <= amount:
            return False
        else:
            self.balance -= amount
            self.save()
            return True

    def __str__(self):
        return (self.user.first_name +" "+ self.user.last_name)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)
    instance.customuser.save()
