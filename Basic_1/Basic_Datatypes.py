# Doing some basic calculations
n1 = 15
n2 = 20
print (n1 + n2) # non decimal value gives non decimal result
print (n2 * 2.5) # if any value is decimal then result will show in decimal
print (n1 ** n2) # double asterisk means power calculation in Python.
username = "Learning Python"
print (len(username)) # length method tells you the length of the string. String is immutable value.
print (username[5]) # here string is treated as array of lisk list datatype.
# Negative concept
print (username[-2]) # minus sign means it starts counting from right side
print (username[2:8]) # from second position to seventh position
# print (dir(username)) # see all the possible methods
mylist = [69, 'Practice', 2.5]
print (mylist)
contacts = {'name':'Anish Sharma', 'age': 32, 'institution': 'Jetking'} # Dictionary datatype
print(contacts['age'], contacts['name'])
x = 5
y = 8
z = 12

# Comparision in PYTHON
# In python comparison operators literally gives BOOLEAN value. True (1) or False (0)
print ("(1 <  2)", 1 < 2)
print ("(5.0 == 5.0)", 5.0 == 5.0)
print ("(4.0 != 5.0)", 4.0 != 5.0)
print ("x < y < z", x < y and y < z) # both are same meaning . 1st one is shorthand method.
# Important Understanding
print ("Why (1 == 2 < 3) is", 1 == 2 < 3)
print ("(1 == 2 and 2 < 3) this is how actually compiler interprates above line")

# Some highly useful and important libraries used in Python
import math
print ("math.floor(3.5) function will give",math.floor(3.5)) # Why? Because floor() always gives the bottom value
print ("math.floor(-4.5) will give ",math.floor(-4.5)) # Again gives closest bottom value.
print ("math.trunc(-4.5) will give",math.trunc(-4.5)) # trunc() always take you close towards Zero (0) value.
print ("math.trunc(3.5) will give",math.trunc(3.5))

import random
print (random.randint(1, 125)) # Every time I run the code it will generate a randome integer value wihin the range of 1 to 125
some_names = ["Sanu", "Shilachi","Akash","Gourab","Deep","Dipyamaan","Saugata","Gopal","Anuradha","Nirban","Souvik","Supriyo"]
print ("random.choice() method is called. Output is :",random.choice(some_names))
# As Python works with various types of numbers it supports OCTAL, HEXADECIMAL, IMAGINARY NUMBERS as well
print ("oct(120) to find out Octal value of 120 which is ",oct(120))
print ("hex(120) to find out Hexadecimal value of 120 which is ",hex(120))
print ("bin(120) to find out Binary value of 120 which is ",bin(120))
print ("=========================== List before shuffeling is done ==============================")
print (some_names)
# Also can use random.shuffle method
random.shuffle(some_names) # Every time it will change when I run the programme
print ("=========================== List after shuffeling is done ===============================")
print (some_names)

# To work best with decimal numbers in Python we need to import decimal library
from decimal import Decimal # To know more read Decimal Context Manager
caldec = Decimal('0.1') + Decimal('0.2') + Decimal('0.3') - Decimal('0.8') # proper decimal calculation in python looks like
print (caldec)
# If we don't import Decimal then what happens?
print (0.1 + 0.2 + 0.3 - 0.8) # What is this?

# To work best with fraction numbers in Python we need to import fraction library
from fractions import Fraction
print ("Fraction (5, 36) will show as ", Fraction (5, 36))