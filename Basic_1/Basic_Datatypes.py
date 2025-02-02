# Doing some basic calculations
n1 = 15
n2 = 20
print (n1+n2) # non decimal value gives non decimal result
print (n2 * 2.5) # if any value is decimal then result will show in decimal
print (n1 ** n2) # double asterisk means power calculation in Python.
username = "Learning Python"
print (len(username)) # length method tells you the length of the string. String is immutable value.
print (username[5]) # here string is treated as array of lisk list datatype.
# Negative concept
print (username[-2]) # minus sign means it starts counting from right side
print (username[2:8]) # from second position to seventh position
#print (dir(username)) # see all the possible methods
mylist = [69, 'Practice', 2.5]
print (mylist)
contacts = {'name':'Anish Sharma', 'age': 32, 'institution': 'Jetking'} # Dictionary datatype
print(contacts['age'], contacts['name'])