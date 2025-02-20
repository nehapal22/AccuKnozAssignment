#import necessary Django modules
from django.db import transaction #handling database transactions
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

#defining signal handler
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    """
    This function is triggered whenever a new User instance is saved.
    It will print whether the signal is running inside a database transaction.
    """
    print(f"Signal received inside transaction: {transaction.get_connection().in_atomic_block}")

# Testing:
with transaction.atomic(): # Start a database transaction
    user = User.objects.create(username="test_user", password="password") #create new user
    print(f"Inside transaction: {transaction.get_connection().in_atomic_block}") #checking if we are inside the transaction
