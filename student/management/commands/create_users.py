from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import random

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):  #mandatory method when arguments to be passed
        parser.add_argument('total_no_user', type=int, help= "Gives total number of users to be created")
        
    def handle(self, *args, **kwargs):
        total_no_user = kwargs['total_no_user']

        for _ in range(total_no_user):
            rand_name = get_random_string(random.randint(5, 7))
            User.objects.create_user(username= rand_name, email= rand_name.lower()+"@gmai.com", password= "Python_123")

        
# Command while running this command line arg - python manage.py create_users 5
# Here, 10 is the value of the total_no_user argument.
# In the handle method, the command-line arguments are accessed through the kwargs dictionary. 
# The keys of this dictionary are the argument names (i.e. total_no_user), and the values are the provided values.(i.e. 5)

# Here, kwargs['total_no_user'] is retrieving the value associated with the key 'total_no_user' from the kwargs dictionary.