
import random
import string
def index(name):
    return f'Your name is {name}'



def password(lenght=5):
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=lenght))
    
