import string
import random
print("Hello, This program will help generate a secure password. Please add some symbols to the end of this password to ensure security.")
x = (random.randint(1,10000))
y = x*(random.randint(1,10000))
random.choice(string.ascii_letters)
print ("Your random password is: ",random.choice(string.ascii_letters),random.choice(string.ascii_letters),random.choice(string.ascii_letters),random.choice(string.ascii_letters),random.choice(string.ascii_letters),random.choice(string.ascii_letters),y)
