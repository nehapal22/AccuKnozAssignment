from django.db.models.signals import post_save #This is a Django signal that is sent after a model's save() method is called
from django.dispatch import receiver #this is a decorator used to connect a signal to a handler function.
from django.contrib.auth.models import User #for user model
import time # this introduces delays

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received ")
    time.sleep(5)  # Simulating a delay
    print("Signal processing complete.")

# Testing:
user = User.objects.create(username="test_user", password="password")# creating a user
print("User is created.") 
