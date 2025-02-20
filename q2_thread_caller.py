import threading #import the threading module
from django.db.models.signals import post_save #import the post_save signal
from django.dispatch import receiver #import the receiver decorator
from django.contrib.auth.models import User #import user model

#connecting signal handler to the post_save signal for the user model
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
     """
     Signal handler function that runs when a user object is saved
     and it prints the name of the thread in which the signal handler is running.
    """
     print(f"signal running in thread: {threading.current_thread().name}")

# Testing:
print(f"Main thread: {threading.current_thread().name}") #printing name of the main thread
user = User.objects.create(username = "test_user", password = "password")#create new user object
